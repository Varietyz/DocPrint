class FormatterResolver:
    def __init__(self):
        self._formatters = {}
    
    def register_formatter(self, name, formatter):
        self._formatters[name] = formatter
    
    def format_section(self, section_type, header, content="", line=True, **kwargs):
        for formatter in self._formatters.values():
            if hasattr(formatter, 'can_handle') and formatter.can_handle(section_type):
                return formatter.format_section(section_type, header, content, line, **kwargs)
        
        return self._formatters.get('basic_content').format_section("text", header, content, line, **kwargs)