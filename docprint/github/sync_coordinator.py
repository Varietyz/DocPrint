from ..config import DOC_FILE_PREFIX, DOC_FILE_EXTENSION

class SyncCoordinator:
    def __init__(self, content_reader, change_detector, api_client, file_handler):
        self.content_reader = content_reader
        self.change_detector = change_detector
        self.api_client = api_client
        self.file_handler = file_handler
    
    def sync_if_changed(self):
        current_content = self.content_reader.get_current_file_content()
        if not current_content:
            return
        
        if not self.change_detector.has_content_changed(current_content):
            return
        
        file_path = self.file_handler.current_filename or f"{DOC_FILE_PREFIX}{DOC_FILE_EXTENSION}"
        if self.api_client.push_content(file_path, current_content):
            self.change_detector.update_synced_hash(current_content)