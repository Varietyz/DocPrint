from .base import BaseFormatter

class FlexLayoutFormatter(BaseFormatter):
    def __init__(self, block_formatter):
        self.block_formatter = block_formatter
    
    def can_handle(self, section_type):
        return section_type == "flex_layout"
    
    def format_section(self, section_type, header, content="", line=True, **kwargs):
        if section_type != "flex_layout":
            return self._format_default(header, content, line, **kwargs)
        
        result = self._create_header(header)
        
        if not isinstance(content, list):
            return self._format_default(header, content, line, **kwargs)
        
        container_style = kwargs.get('container_style', 'display: flex; gap: 20px;')
        result += f'<div style="{container_style}">\n\n'
        
        for block in content:
            if not isinstance(block, dict):
                continue
                
            block_type = block.get('type', 'text')
            block_header = block.get('header', '')
            block_content = block.get('content', '')
            block_style = block.get('style', '')
            block_kwargs = block.get('kwargs', {})
            
            div_style = f'flex: 1; {block_style}' if block_style else 'flex: 1;'
            result += f'<div style="{div_style}">\n\n'
            
            formatted_block = self.block_formatter.format_block(block_type, block_header, block_content, **block_kwargs)
            result += formatted_block
            
            result += '\n</div>\n\n'
        
        result += '</div>\n\n'
        return self._add_line_if_needed(result, line, **kwargs)