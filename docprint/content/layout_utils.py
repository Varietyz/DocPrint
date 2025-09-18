from ..utils.regex_utils import get_regex

class LayoutUtils:
    @staticmethod
    def is_layout_content(content):
        return ('<div style=' in content and 
                ('display: flex' in content or 'display: grid' in content)) or '<table style=' in content
    
    @staticmethod
    def normalize_layout_content(content):
        re = get_regex()
        normalized = content.strip()
        normalized = re.sub(r'\s*\n\s*', '\n', normalized)
        normalized = re.sub(r'\n{3,}', '\n\n', normalized)
        return normalized