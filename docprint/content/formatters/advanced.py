from .base import BaseFormatter

class AdvancedFormatters(BaseFormatter):
    def can_handle(self, section_type):
        return section_type in {"footnotes", "definition_list", "task_list"}
    
    def format_section(self, section_type, header, content="", line=True, **kwargs):
        formatters = {
            "footnotes": self._format_footnotes,
            "definition_list": self._format_definition_list,
            "task_list": self._format_task_list
        }
        
        formatter = formatters.get(section_type)
        if formatter:
            return formatter(header, content, line, **kwargs)
        return self._format_default(header, content, line, **kwargs)
    
    def _format_footnotes(self, header, content, line, **kwargs):
        result = self._create_header(header)
        
        if isinstance(content, tuple) and len(content) == 2:
            main_text, footnotes = content
            definitions = []
            
            for num, note_content in footnotes.items():
                main_text += f"[^{num}]"
                definitions.append(f"[^{num}]: {note_content}")
            
            result += main_text + "\n\n"
            result += "\n".join(definitions) + "\n\n"
        else:
            result += f"{content}\n\n"
        
        return self._add_line_if_needed(result, line, **kwargs)
    
    def _format_definition_list(self, header, content, line, **kwargs):
        result = self._create_header(header)
        
        if isinstance(content, dict):
            for term, definition in content.items():
                result += f"{term}\n: {definition}\n\n"
        else:
            result += f"{content}\n\n"
        
        return self._add_line_if_needed(result, line, **kwargs)
    
    def _format_task_list(self, header, content, line, **kwargs):
        result = self._create_header(header)
        
        if isinstance(content, list):
            for item in content:
                if isinstance(item, dict):
                    status = "[x]" if item.get('completed', False) else "[ ]"
                    result += f"- {status} {item.get('task', '')}\n"
                else:
                    result += f"- {item}\n"
            result += "\n"
        else:
            result += f"{content}\n\n"
        
        return self._add_line_if_needed(result, line, **kwargs)