from fp_py.internals._prop import _get_prop, _prop_equals

def _where(props:dict, search_obj:dict):
    return all({ fn(_get_prop(key, search_obj)) for key, fn in props.items() })


def _where_equals(props:dict, search_obj:dict):
    return all({ _prop_equals(val, key, search_obj) for key, val in props.items() })
