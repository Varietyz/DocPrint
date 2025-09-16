from .base import BaseFormatter

class BasicContentFormatter(BaseFormatter):
    def format_section(self, section_type, header, content="", line=True, **kwargs):
        formatters = {
            "header": self._format_header,
            "table": self._format_table,
            "text": self._format_text
        }
        
        formatter = formatters.get(section_type)
        if formatter:
            return formatter(header, content, line, **kwargs)
        return self._format_text(header, content, line)
    
    def _format_header(self, header, content, line):
        header_line = f"## {header}\n\n"
        if line and content:
            header_line += f"{content}\n\n"
        elif content:
            header_line += f"{content}\n\n"
        return header_line
    
    def _format_table(self, header, content, line, **kwargs):
        result = f"## {header}\n\n"
        if isinstance(content, list) and len(content) > 0:
            if isinstance(content[0], dict):
                headers = list(content[0].keys())
                result += "| " + " | ".join(headers) + " |\n"
                result += "|" + "---|" * len(headers) + "\n"
                for row in content:
                    values = [str(row.get(h, "")) for h in headers]
                    result += "| " + " | ".join(values) + " |\n"
            else:
                result += str(content) + "\n"
        else:
            result += str(content) + "\n"
        return result + "\n"
    
    def _format_text(self, header, content, line):
        result = f"## {header}\n\n"
        if line:
            result += f"{content}\n\n---\n\n"
        else:
            result += f"{content}\n\n"
        return result