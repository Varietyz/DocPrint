from pathlib import Path
from docprint import docPrint, docFlush, docPrintFile

class FileManagementTest:
    def run(self):
        self._test_custom_files()
        self._test_directory_creation()
        self._test_file_reset()
    
    def _test_custom_files(self):
        print("Testing file management...")
        
        docPrintFile("test_custom.md")
        docPrint('text', 'Custom File Test', 'This is in a custom file')
        docFlush()
        
        custom_file = Path('test_custom.md')
        if not custom_file.exists():
            raise AssertionError("Custom file not created")
        
        content = custom_file.read_text(encoding='utf-8')
        if 'Custom File Test' not in content:
            raise AssertionError("Custom file content missing")
        
        print("  Custom file creation works")
    
    def _test_directory_creation(self):
        docPrintFile("test_dir/nested/deep.md")
        docPrint('text', 'Deep File', 'Nested directory test')
        docFlush()
        
        deep_file = Path('test_dir/nested/deep.md')
        if not deep_file.exists():
            raise AssertionError("Nested directory file not created")
        
        if not deep_file.parent.exists():
            raise AssertionError("Nested directory not created")
        
        print("  Directory creation works")
    
    def _test_file_reset(self):
        docPrintFile("")
        docPrint('text', 'Back to Default', 'Should be in DOC.PRINT.md')
        docFlush()
        
        default_file = Path('DOC.PRINT.md')
        content = default_file.read_text(encoding='utf-8')
        if 'Back to Default' not in content:
            raise AssertionError("File reset failed")
        
        print("  File management works")