from ..utils.hashing import hash_content

class ChangeDetector:
    def __init__(self):
        self.last_synced_hash = None
    
    def has_content_changed(self, content):
        if not content:
            return False
        
        current_hash = hash_content(content)
        if current_hash == self.last_synced_hash:
            return False
        
        return True
    
    def update_synced_hash(self, content):
        self.last_synced_hash = hash_content(content)