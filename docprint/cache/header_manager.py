class HeaderManager:
    def __init__(self):
        self.header_cache = set()
    
    def ensure_unique_header(self, original_header):
        if original_header not in self.header_cache:
            return original_header
        
        counter = 1
        while f"{original_header} ({counter})" in self.header_cache:
            counter += 1
        
        return f"{original_header} ({counter})"
    
    def add_header(self, header):
        self.header_cache.add(header)
    
    def clear_cache(self):
        self.header_cache.clear()