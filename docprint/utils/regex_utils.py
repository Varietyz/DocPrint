from .fallback_utils import try_import_fallback

re = try_import_fallback('regex', 're')

def get_regex():
    return re