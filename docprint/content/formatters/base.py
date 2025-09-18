from .utils import FormatterUtils

class BaseFormatter:
    def format_section(self, section_type, header, content="", line=True, **kwargs):
        raise NotImplementedError("Subclasses must implement format_section")
    
    def _create_header(self, header):
        return FormatterUtils.create_header(header)
    
    def _add_content_with_line(self, result, content, line):
        return FormatterUtils.add_content_with_line(result, content, line)
    
    def _ensure_newline_separation(self, result):
        return FormatterUtils.ensure_newline_separation(result)
    
    def _add_line_if_needed(self, result, line, **kwargs):
        if line:
            divider_line = kwargs.get('divider_line')
            if divider_line:
                divider_html = self._get_divider_formatter().format_divider_line(**divider_line)
                return result + divider_html + "\n\n"
            else:
                return result + "---\n\n"
        return result
    
    def _get_divider_formatter(self):
        from .divider import DividerFormatter
        if not hasattr(self, '_divider_formatter'):
            self._divider_formatter = DividerFormatter()
        return self._divider_formatter
    
    def _format_default(self, header, content, line, **kwargs):
        result = self._create_header(header)
        return self._add_content_with_line(result, content, line)