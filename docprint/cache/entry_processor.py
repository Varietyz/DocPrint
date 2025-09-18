import time
from ..content.layout_utils import LayoutUtils
from ..utils.hashing import hash_content

class CacheEntryProcessor:
    def process_entry(self, header, content, unique_header):
        updated_content = content.replace(f"## {header}", f"## {unique_header}", 1) if header != unique_header else content
        
        if LayoutUtils.is_layout_content(updated_content):
            normalized_content = LayoutUtils.normalize_layout_content(updated_content)
            content_hash = hash_content(normalized_content)
        else:
            content_hash = hash_content(updated_content)
        
        return {
            'header': unique_header,
            'content': updated_content,
            'timestamp': time.time(),
            'hash': content_hash
        }