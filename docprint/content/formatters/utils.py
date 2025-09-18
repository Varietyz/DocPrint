class FormatterUtils:
    @staticmethod
    def create_header(header):
        return f"## {header}\n\n"
    
    @staticmethod
    def add_content_with_line(result, content, line):
        if line and content:
            return result + f"{content}\n\n---\n\n"
        elif content:
            return result + f"{content}\n\n"
        return result
    
    @staticmethod
    def ensure_newline_separation(result):
        if result and not result.endswith('\n'):
            return result + '\n'
        return result