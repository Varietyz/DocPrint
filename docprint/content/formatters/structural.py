from .base import BaseFormatter

class StructuralFormatter(BaseFormatter):
    def format_section(self, section_type, header, content="", line=True, **kwargs):
        formatters = {
            "bullets": self._format_bullets,
            "horizontal_rule": self._format_horizontal_rule,
            "code_block": self._format_code_block,
            "blockquote": self._format_blockquote,
            "ordered_list": self._format_ordered_list,
            "unordered_list": self._format_unordered_list
        }
        
        formatter = formatters.get(section_type)
        if formatter:
            return formatter(header, content, line, **kwargs)
        return self._format_default(header, content, line)
    
    def _format_bullets(self, header, content, line, **kwargs):
        result = self._create_header(header)
        if isinstance(content, list):
            for item in content:
                result += f"- {item}\n"
            result += "\n"
        else:
            result += f"- {content}\n\n"
        return self._add_line_if_needed(result, line)
    
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
        return self._add_line_if_needed(result, line)
    
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
        return self._add_line_if_needed(result, line)
    
    def _format_ordered_list(self, header, content, line, **kwargs):
        result = self._create_header(header)
        if isinstance(content, list):
            for i, item in enumerate(content, 1):
                result += f"{i}. {item}\n"
            result += "\n"
        else:
            result += f"1. {content}\n\n"
        return self._add_line_if_needed(result, line)
    
    def _format_unordered_list(self, header, content, line, **kwargs):
        result = self._create_header(header)
        if isinstance(content, list):
            for item in content:
                result += f"- {item}\n"
            result += "\n"
        else:
            result += f"- {content}\n\n"
        return self._add_line_if_needed(result, line)
    
    def _format_default(self, header, content, line):
        result = self._create_header(header)
        return self._add_content_with_line(result, content, line)
    
    def _add_line_if_needed(self, result, line):
        if line:
            return result + "---\n\n"
        return result