from .base import BaseFormatter

class GridLayoutFormatter(BaseFormatter):
    def __init__(self, block_formatter):
        self.block_formatter = block_formatter
    
    def can_handle(self, section_type):
        return section_type == "grid_layout"
    
    def format_section(self, section_type, header, content="", line=True, **kwargs):
        if section_type != "grid_layout":
            return self._format_default(header, content, line, **kwargs)
        
        result = self._create_header(header)
        
        if not isinstance(content, list):
            return self._format_default(header, content, line, **kwargs)
        
        columns = kwargs.get('columns', 2)
        gap = kwargs.get('gap', '20px')
        container_style = f'display: grid; grid-template-columns: repeat({columns}, 1fr); gap: {gap};'
        
        result += f'<div style="{container_style}">\n\n'
        
        for block in content:
            if not isinstance(block, dict):
                continue
                
            block_type = block.get('type', 'text')
            block_header = block.get('header', '')
            block_content = block.get('content', '')
            block_style = block.get('style', '')
            block_kwargs = block.get('kwargs', {})
            
            result += f'<div style="{block_style}">\n\n'
            
            formatted_block = self.block_formatter.format_block(block_type, block_header, block_content, **block_kwargs)
            result += formatted_block
            
            result += '\n</div>\n\n'
        
        result += '</div>\n\n'
        return self._add_line_if_needed(result, line, **kwargs)