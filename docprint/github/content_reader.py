class ContentReader:
    def __init__(self, file_handler):
        self.file_handler = file_handler
    
    def get_current_file_content(self):
        try:
            if self.file_handler.target_file.exists():
                return self.file_handler.target_file.read_text(encoding='utf-8')
        except Exception:
            pass
        return ""