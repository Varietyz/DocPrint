import mmap
from pathlib import Path
from ..config import DEFAULT_OUTPUT_DIR, DOC_FILE_PREFIX, DOC_FILE_EXTENSION
from ..content.matcher import ContentMatcher

class FileHandler:
    def __init__(self, output_dir=DEFAULT_OUTPUT_DIR):
        self.output_dir = Path(output_dir)
        self.content_matcher = ContentMatcher()
        self.current_filename = None
        self._set_default_target_file()
    
    def _set_default_target_file(self):
        self.current_filename = f"{DOC_FILE_PREFIX}{DOC_FILE_EXTENSION}"
        self.target_file = self.output_dir / self.current_filename
    
    def set_output_filename(self, filepath):
        if not filepath or filepath == "." or filepath == "..":
            self._set_default_target_file()
            print(f"Reset to default file: {self.target_file}")
            return
        
        if any(char in filepath for char in ['<', '>', ':', '"', '|', '?', '*']):
            raise ValueError(f"Invalid filename characters: {filepath}")
        
        full_path = self.output_dir / filepath
        
        full_path.parent.mkdir(parents=True, exist_ok=True)
        
        self.target_file = full_path
        self.current_filename = filepath
        print(f"Output file set to: {filepath}")
    
    def write_cached_content(self, cache_entries):
        if not cache_entries:
            return
        
        for entry in cache_entries:
            self._write_entry(entry['header'], entry['content'])
    
    def _write_entry(self, header, content):
        self.target_file.parent.mkdir(parents=True, exist_ok=True)
        
        if self.target_file.exists():
            self._update_existing_file(self.target_file, header, content)
        else:
            self._create_new_file(self.target_file, header, content)
    
    def _update_existing_file(self, file_path, header, new_content):
        existing_content = self._read_file(file_path)
        updated_content = self.content_matcher.update_or_append(
            existing_content, header, new_content
        )
        self._write_file(file_path, updated_content)
    
    def _create_new_file(self, file_path, header, content):
        self._write_file(file_path, content)
    
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
        except Exception:
            return ""
    
    def _write_file(self, file_path, content):
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content, encoding='utf-8')