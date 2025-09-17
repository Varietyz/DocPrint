import shutil
from pathlib import Path

class TestCleanup:
    def __init__(self):
        self.test_files = [
            'DOC.PRINT.md',
            'test_custom.md',
            'github_test.md'
        ]
        
        self.test_dirs = [
            'test_dir'
        ]
    
    def cleanup_all(self):
        print("Cleaning up test files...")
        
        self._remove_files()
        self._remove_directories()
        
        print("  Test files cleaned up")
    
    def _remove_files(self):
        for file_path in self.test_files:
            try:
                Path(file_path).unlink(missing_ok=True)
            except Exception:
                pass
    
    def _remove_directories(self):
        for dir_path in self.test_dirs:
            try:
                shutil.rmtree(dir_path, ignore_errors=True)
            except Exception:
                pass