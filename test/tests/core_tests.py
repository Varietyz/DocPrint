from pathlib import Path
from docprint import docPrint, flush_cache

class CoreFunctionalityTest:
    def run(self):
        self._test_basic_functionality()
        self._test_content_updates()
        self._test_content_deduplication()
        self._test_error_handling()
    
    def _test_basic_functionality(self):
        print("Testing basic functionality...")
        
        docPrint('header', 'Test Header', 'Test content', line=True)
        docPrint('text', 'Status Update', 'System operational', line=False)
        docPrint('table', 'Performance Data', [
            {'metric': 'CPU', 'value': '45%'},
            {'metric': 'Memory', 'value': '2.1GB'}
        ], line=True)
        
        flush_cache()
        
        doc_file = Path('DOC.PRINT.md')
        if not doc_file.exists():
            raise AssertionError("DOC.PRINT.md not created")
        
        content = doc_file.read_text(encoding='utf-8')
        if '## Test Header' not in content:
            raise AssertionError("Header formatting failed")
        if '## Status Update' not in content:
            raise AssertionError("Text formatting failed")
        if 'CPU' not in content:
            raise AssertionError("Table formatting failed")
        
        print("  Basic formatting works")
    
    def _test_content_updates(self):
        print("Testing content updates...")
        
        docPrint('header', 'Update Test', 'Initial content', line=True)
        flush_cache()
        
        docPrint('header', 'Update Test', 'Updated content', line=True)
        flush_cache()
        
        content = Path('DOC.PRINT.md').read_text(encoding='utf-8')
        if 'Updated content' not in content:
            raise AssertionError("Content update failed")
        if 'Initial content' in content:
            raise AssertionError("Old content not replaced")
        
        print("  Content updates work")
    
    def _test_content_deduplication(self):
        print("Testing content deduplication...")
        
        docPrint('text', 'Dedup Test', 'Same content', line=False)
        flush_cache()
        
        docPrint('text', 'Dedup Test', 'Same content', line=False)
        flush_cache()
        
        print("  Content deduplication works")
    
    def _test_error_handling(self):
        print("Testing error handling...")
        
        docPrint('text', 'Empty Test', '', line=True)
        flush_cache()
        
        docPrint('text', 'None Test', None, line=True)
        flush_cache()
        
        docPrint('table', 'Complex Data', [], line=False)
        flush_cache()
        
        docPrint('unknown_type', 'Fallback Test', 'Should fall back to text format')
        flush_cache()
        
        print("  Error handling works")