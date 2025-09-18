def try_import_fallback(*modules):
    for module_name in modules:
        try:
            return __import__(module_name)
        except ImportError:
            continue
    raise ImportError(f"None of the modules {modules} could be imported")

def create_fallback_functions(fallback_map):
    for module_names, func_dict in fallback_map.items():
        try:
            if isinstance(module_names, str):
                module_names = (module_names,)
            
            for module_name in module_names:
                try:
                    module = __import__(module_name)
                    return func_dict[module_name](module)
                except ImportError:
                    continue

            fallback_name = list(func_dict.keys())[-1]
            module = __import__(fallback_name)
            return func_dict[fallback_name](module)
        except ImportError:
            raise ImportError(f"No suitable module found for {module_names}")