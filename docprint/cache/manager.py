from ..files.handler import FileHandler
from .header_manager import HeaderManager
from .entry_processor import CacheEntryProcessor
from .storage import CacheStorage
from .flush_coordinator import FlushCoordinator

class CacheManager:
    def __init__(self):
        self.header_manager = HeaderManager()
        self.entry_processor = CacheEntryProcessor()
        self.storage = CacheStorage()
        self.file_handler = FileHandler()
        self.flush_coordinator = FlushCoordinator(self.storage, self.file_handler)
    
    def add_entry(self, header, content):
        unique_header = self.header_manager.ensure_unique_header(header)
        self.header_manager.add_header(unique_header)
        
        entry = self.entry_processor.process_entry(header, content, unique_header)
        self.storage.add_entry(entry)
        
        if self.flush_coordinator.flush_controller is None:
            self.flush_coordinator.initialize_flush_controller(self)
        
        self.flush_coordinator.check_flush_conditions()
        return unique_header
    
    def flush(self):
        self.flush_coordinator.flush()
    
    def clear_header_cache(self):
        self.header_manager.clear_cache()