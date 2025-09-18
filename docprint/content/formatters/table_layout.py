from .base import BaseFormatter

class TableLayoutFormatter(BaseFormatter):
    def __init__(self, block_formatter):
        self.block_formatter = block_formatter
    
    def can_handle(self, section_type):
        return section_type == "table_layout"
    
    def format_section(self, section_type, header, content="", line=True, **kwargs):
        if section_type != "table_layout":
            return self._format_default(header, content, line, **kwargs)
        
        result = self._create_header(header)
        
        if not isinstance(content, list):
            return self._format_default(header, content, line, **kwargs)
        
        table_style = kwargs.get('table_style', 'width: 100%; border-collapse: collapse;')
        result += f'<table style="{table_style}">\n<tr>\n'
        
        for block in content:
            if not isinstance(block, dict):
                continue
                
            block_type = block.get('type', 'text')
            block_header = block.get('header', '')
            block_content = block.get('content', '')
            cell_style = block.get('style', '')
            block_kwargs = block.get('kwargs', {})
            
            td_style = f'vertical-align: top; padding: 10px; {cell_style}' if cell_style else 'vertical-align: top; padding: 10px;'
            result += f'<td style="{td_style}">\n\n'
            
            formatted_block = self.block_formatter.format_block(block_type, block_header, block_content, **block_kwargs)
            result += formatted_block
            
            result += '\n</td>\n'
        
        result += '</tr>\n</table>\n\n'
        return self._add_line_if_needed(result, line, **kwargs)