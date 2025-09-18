import mmap
import threading
from pathlib import Path
from ..config import DEFAULT_OUTPUT_DIR, DOC_FILE_PREFIX, DOC_FILE_EXTENSION
from ..content.matcher import ContentMatcher
from ..utils.file_utils import atomic_write_file
from ..utils.validation_utils import ValidationUtils
from ..utils.error_utils import ErrorReporter

class FileHandler:
    def __init__(self, output_dir=DEFAULT_OUTPUT_DIR):
        self.output_dir = Path(output_dir)
        self.content_matcher = ContentMatcher()
        self.current_filename = None

        self._in_memory_content = None
        self._file_loaded = False
        self._lock = threading.RLock()

        self._set_default_target_file()

    def _set_default_target_file(self):
        self.current_filename = f"{DOC_FILE_PREFIX}{DOC_FILE_EXTENSION}"
        self.target_file = self.output_dir / self.current_filename
        with self._lock:
            self._in_memory_content = None
            self._file_loaded = False

    def set_output_filename(self, filepath):
        is_valid, error_msg = ValidationUtils.validate_filename(filepath)
        if not is_valid:
            if filepath in (".", "..") or not filepath:
                self._set_default_target_file()
                print(f"Reset to default file: {self.target_file}")
                return
            raise ValueError(error_msg)

        full_path = self.output_dir / filepath
        full_path.parent.mkdir(parents=True, exist_ok=True)

        self.target_file = full_path
        self.current_filename = filepath

        with self._lock:
            self._in_memory_content = None
            self._file_loaded = False

        print(f"Output file set to: {filepath}")

    def write_cached_content(self, cache_entries):
        if not cache_entries:
            return

        self._ensure_content_loaded()

        with self._lock:
            for entry in cache_entries:
                self._in_memory_content = self.content_matcher.update_or_append(
                    self._in_memory_content, entry['header'], entry['content']
                )

            atomic_write_file(self.target_file, self._in_memory_content)

    def _ensure_content_loaded(self):
        with self._lock:
            if self._file_loaded:
                return

            if self.target_file.exists():
                try:
                    self._in_memory_content = self._read_file(self.target_file)
                except Exception as e:
                    fallback = lambda: ""
                    self._in_memory_content = ErrorReporter.report_file_error(
                        "read", self.target_file, e, fallback
                    ) or ""
            else:
                self._in_memory_content = ""

            self._file_loaded = True

    def _read_file(self, file_path):
        try:
            file_stat = file_path.stat()
            file_size = file_stat.st_size

            if file_size == 0:
                return ""

            if file_size > 1024 * 1024:
                with file_path.open('rb') as f:
                    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
                        return mm.read().decode('utf-8')
            else:
                return file_path.read_text(encoding='utf-8')
        except FileNotFoundError:
            return ""
        except Exception as e:
            ErrorReporter.report_file_error("read", file_path, e)
            return ""

    def _write_entry(self, header, content):
        self.write_cached_content([{'header': header, 'content': content}])

    def _update_existing_file(self, file_path, header, new_content):
        self.write_cached_content([{'header': header, 'content': new_content}])

    def _create_new_file(self, file_path, header, content):
        self.write_cached_content([{'header': header, 'content': content}])