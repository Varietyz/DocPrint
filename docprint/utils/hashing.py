from .fallback_utils import create_fallback_functions

def _xxhash_impl(xxhash):
    def hash_content(content):
        return xxhash.xxh64(content.encode('utf-8')).hexdigest()
    return hash_content

def _hashlib_impl(hashlib):
    def hash_content(content):
        return hashlib.md5(content.encode('utf-8')).hexdigest()
    return hash_content

hash_content = create_fallback_functions({
    ('xxhash', 'hashlib'): {
        'xxhash': _xxhash_impl,
        'hashlib': _hashlib_impl
    }
})