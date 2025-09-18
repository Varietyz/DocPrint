from ..config.constants import CACHE_FLUSH_INTERVAL, CACHE_FLUSH_COUNT

class FlushCoordinator:
    def __init__(self, storage, file_handler):
        self.storage = storage
        self.file_handler = file_handler
        self.flush_controller = None
    
    def check_flush_conditions(self):
        time_elapsed = self.storage.get_time_since_flush()
        if (time_elapsed >= CACHE_FLUSH_INTERVAL or 
            self.storage.call_count >= CACHE_FLUSH_COUNT):
            self.flush()
    
    def flush(self):
        if self.storage.is_empty():
            return
        
        entries = self.storage.get_entries()
        self.file_handler.write_cached_content(entries)
        self.storage.clear()
    
    def initialize_flush_controller(self, cache_manager):
        if self.flush_controller is None:
            from .flush import FlushController
            self.flush_controller = FlushController(cache_manager)
            self.flush_controller.start_timer()