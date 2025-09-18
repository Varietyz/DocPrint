from .base import BaseFormatter

class ListFormatters(BaseFormatter):
    def can_handle(self, section_type):
        return section_type in {"bullets", "ordered_list", "unordered_list"}
    
    def format_section(self, section_type, header, content="", line=True, **kwargs):
        formatters = {
            "bullets": self._format_bullets,
            "ordered_list": self._format_ordered_list,
            "unordered_list": self._format_unordered_list
        }
        
        formatter = formatters.get(section_type)
        if formatter:
            return formatter(header, content, line, **kwargs)
        return self._format_default(header, content, line, **kwargs)
    
    def _format_bullets(self, header, content, line, **kwargs):
        result = self._create_header(header)
        if isinstance(content, list):
            for item in content:
                result += f"- {item}\n"
            result += "\n"
        else:
            result += f"- {content}\n\n"
        return self._add_line_if_needed(result, line, **kwargs)
    
    def _format_ordered_list(self, header, content, line, **kwargs):
        result = self._create_header(header)
        if isinstance(content, list):
            for i, item in enumerate(content, 1):
                result += f"{i}. {item}\n"
            result += "\n"
        else:
            result += f"1. {content}\n\n"
        return self._add_line_if_needed(result, line, **kwargs)
    
    def _format_unordered_list(self, header, content, line, **kwargs):
        result = self._create_header(header)
        if isinstance(content, list):
            for item in content:
                result += f"- {item}\n"
            result += "\n"
        else:
            result += f"- {content}\n\n"
        return self._add_line_if_needed(result, line, **kwargs)