from ..cache.manager import CacheManager
from ..content.formatters import UnifiedFormatter
from ..files.handler import FileHandler

class DocPrintManager:
    def __init__(self):
        self.cache_manager = None
        self.unified_formatter = None
        self.file_handler = None
        self.current_filepath = None

    def initialize(self):
        if self.cache_manager is None:
            self.cache_manager = CacheManager()

        if self.unified_formatter is None:
            self.unified_formatter = UnifiedFormatter()

        if self.file_handler is None:
            self.file_handler = FileHandler()
            self.cache_manager.file_handler = self.file_handler

    def docPrint(self, section_type, header, content="", line=True, **kwargs):
        self.initialize()

        formatted_content = self.unified_formatter.format_section(
            section_type, header, content, line, **kwargs
        )

        self.cache_manager.add_entry(header, formatted_content)

    def docPrintFile(self, filepath):
        self.initialize()

        if self.cache_manager.cache:
            self.flush_cache()

        self.file_handler.set_output_filename(filepath)
        self.current_filepath = filepath
        print(f"Output file set to: {filepath}")

    def flush_cache(self):
        if self.cache_manager:
            self.cache_manager.flush()

_docprint_manager = DocPrintManager()

def docPrint(section_type, header, content="", line=True, **kwargs):
    _docprint_manager.docPrint(section_type, header, content, line, **kwargs)

def docPrintFile(filepath):
    _docprint_manager.docPrintFile(filepath)

def flush_cache():
    _docprint_manager.flush_cache()