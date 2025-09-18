from .fallback_utils import create_fallback_functions

def _orjson_impl(orjson):
    def dumps(data):
        return orjson.dumps(data).decode('utf-8')
    def loads(data):
        return orjson.loads(data)
    return dumps, loads

def _ujson_impl(ujson):
    def dumps(data):
        return ujson.dumps(data)
    def loads(data):
        return ujson.loads(data)
    return dumps, loads

def _json_impl(json):
    def dumps(data):
        return json.dumps(data)
    def loads(data):
        return json.loads(data)
    return dumps, loads

dumps, loads = create_fallback_functions({
    ('orjson', 'ujson', 'json'): {
        'orjson': _orjson_impl,
        'ujson': _ujson_impl,
        'json': _json_impl
    }
})