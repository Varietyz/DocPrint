from pathlib import Path
from .error_utils import ErrorReporter

def atomic_write_file(file_path, content):
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    temp_file = file_path.with_suffix('.tmp')
    try:
        temp_file.write_text(content, encoding='utf-8')
        temp_file.replace(file_path)
    except Exception as e:
        def fallback_write():
            file_path.write_text(content, encoding='utf-8')
            return True
        
        def cleanup():
            try:
                temp_file.unlink(missing_ok=True)
            except Exception:
                pass
        
        ErrorReporter.report_file_error("atomic write", file_path, e, fallback_write)
        cleanup()