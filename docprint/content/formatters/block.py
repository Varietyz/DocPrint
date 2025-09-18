class BlockFormatter:
    def __init__(self, resolver):
        self.resolver = resolver
    
    def format_block(self, block_type, block_header, block_content, **kwargs):
        if block_header:
            formatted = self.resolver.format_section(block_type, block_header, block_content, line=False, **kwargs)
            formatted = formatted.replace(f"## {block_header}\n\n", f"### {block_header}\n\n")
            return formatted
        else:
            content_only = self.resolver.format_section(block_type, "temp", block_content, line=False, **kwargs)
            return content_only.replace("## temp\n\n", "", 1)