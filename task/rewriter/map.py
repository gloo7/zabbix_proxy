from task._typing import D, Process
from typing import Callable, Dict


def set_rewriter(*args, key: str, value: str, **kwargs) -> Process:
    def inner(data: D) -> D:
        data[key] = value
        return data

    return inner


def subset_rewriter(*args, key: str, old: str, value: str, **kwargs) -> Process:
    def inner(data: D) -> D:
        if v := data.get(key) is not None:
            data[key] = v.replace(old, value)
        return data

    return inner


def mapping_rewriter(*args, key: str, mapping: Dict[str, str], **kwargs) -> Process:
    def inner(data: D) -> D:
        if val := data.get(key) is None:
            return data
        if new_val := mapping.get(val) is not None:
            data[key] = new_val
        return data
    return inner


rewriter_mapping = {k.rstrip('_rewriter'): globals(
)[k] for k in globals() if k.endswith('_rewriter')}
