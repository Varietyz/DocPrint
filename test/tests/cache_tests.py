import time
from pathlib import Path
from docprint import docPrint, docFlush
from docprint.config import constants

class CacheTest:
    def run(self):
        self._test_cache_timing()
    
    def _test_cache_timing(self):
        print("Testing cache timing...")
        
        original_interval = constants.CACHE_FLUSH_INTERVAL
        original_count = constants.CACHE_FLUSH_COUNT
        
        constants.CACHE_FLUSH_INTERVAL = 2
        constants.CACHE_FLUSH_COUNT = 999
        
        docFlush()
        docPrint('text', 'Timed Entry', 'Should auto-flush after 2 seconds', line=True)
        time.sleep(4)
        
        constants.CACHE_FLUSH_INTERVAL = original_interval
        constants.CACHE_FLUSH_COUNT = original_count
        
        doc_file = Path('DOC.PRINT.md')
        if not doc_file.exists():
            raise AssertionError("Auto-flush timing test failed - no file created")
        
        content = doc_file.read_text(encoding='utf-8')
        if 'Timed Entry' not in content:
            raise AssertionError("Auto-flush timing test failed - content not found")
        
        print("  Auto-flush timing works")