from .visual import VisualFormatter
from .content_basic import BasicContentFormatter
from .content_rich import RichContentFormatter
from .divider import DividerFormatter
from .chart import ChartFormatter
from .resolver import FormatterResolver
from .block import BlockFormatter
from .flex_layout import FlexLayoutFormatter
from .table_layout import TableLayoutFormatter
from .grid_layout import GridLayoutFormatter
from .list import ListFormatters
from .text import TextFormatters
from .advanced import AdvancedFormatters

class UnifiedFormatter:
    def __init__(self):
        self.resolver = FormatterResolver()
        self.block_formatter = BlockFormatter(self.resolver)
        
        self.visual = VisualFormatter()
        self.basic_content = BasicContentFormatter()
        self.rich_content = RichContentFormatter()
        self.divider = DividerFormatter()
        self.chart = ChartFormatter()
        
        self.flex_layout = FlexLayoutFormatter(self.block_formatter)
        self.table_layout = TableLayoutFormatter(self.block_formatter)
        self.grid_layout = GridLayoutFormatter(self.block_formatter)
        self.list_formatters = ListFormatters()
        self.text_formatters = TextFormatters()
        self.advanced_formatters = AdvancedFormatters()
        
        self._register_formatters()
    
    def _register_formatters(self):
        self.resolver.register_formatter('visual', self.visual)
        self.resolver.register_formatter('basic_content', self.basic_content)
        self.resolver.register_formatter('rich_content', self.rich_content)
        self.resolver.register_formatter('divider', self.divider)
        self.resolver.register_formatter('chart', self.chart)
        self.resolver.register_formatter('flex_layout', self.flex_layout)
        self.resolver.register_formatter('table_layout', self.table_layout)
        self.resolver.register_formatter('grid_layout', self.grid_layout)
        self.resolver.register_formatter('list_formatters', self.list_formatters)
        self.resolver.register_formatter('text_formatters', self.text_formatters)
        self.resolver.register_formatter('advanced_formatters', self.advanced_formatters)
    
    def format_section(self, section_type, header, content="", line=True, **kwargs):
        return self.resolver.format_section(section_type, header, content, line, **kwargs)