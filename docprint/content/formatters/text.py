from .base import BaseFormatter

class TextFormatters(BaseFormatter):
    def can_handle(self, section_type):
        return section_type in {"horizontal_rule", "code_block", "blockquote"}
    
    def format_section(self, section_type, header, content="", line=True, **kwargs):
        formatters = {
            "horizontal_rule": self._format_horizontal_rule,
            "code_block": self._format_code_block,
            "blockquote": self._format_blockquote
        }
        
        formatter = formatters.get(section_type)
        if formatter:
            return formatter(header, content, line, **kwargs)
        return self._format_default(header, content, line, **kwargs)
    
    def _format_horizontal_rule(self, header, content, line, **kwargs):
        result = self._create_header(header)
        if content:
            result += f"{content}\n\n"
        result += "---\n\n"
        return result
    
    def _format_code_block(self, header, content, line, **kwargs):
        language = kwargs.get('language', '')
        result = self._create_header(header)
        result += f"```{language}\n{content}\n```\n\n"
        return self._add_line_if_needed(result, line, **kwargs)
    
    def _format_blockquote(self, header, content, line, **kwargs):
        result = self._create_header(header)
        if isinstance(content, list):
            for quote_line in content:
                result += f"> {quote_line}\n"
        else:
            lines = str(content).split('\n')
            for quote_line in lines:
                result += f"> {quote_line}\n"
        result += "\n"
        return self._add_line_if_needed(result, line, **kwargs)