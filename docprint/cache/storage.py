import time

class CacheStorage:
    def __init__(self):
        self.cache = []
        self.content_hashes = {}
        self.call_count = 0
        self.last_flush_time = time.time()
    
    def add_entry(self, entry):
        self.cache.append(entry)
        self.content_hashes[entry['header']] = entry['hash']
        self.call_count += 1
    
    def clear(self):
        self.cache.clear()
        self.call_count = 0
        self.last_flush_time = time.time()
    
    def is_empty(self):
        return len(self.cache) == 0
    
    def get_entries(self):
        return self.cache.copy()
    
    def update_flush_time(self):
        self.last_flush_time = time.time()
    
    def get_time_since_flush(self):
        return time.time() - self.last_flush_time