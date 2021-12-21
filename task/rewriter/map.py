from task._typing import D, Process
from typing import Dict, Any, List


def set_rewriter(*args, key: str, value: str, **kwargs) -> Process:
    def inner(data: D) -> D:
        data[key] = value
        return data

    return inner


def subset_rewriter(*args, key: str, old: str, value: str, **kwargs) -> Process:
    def inner(data: D) -> D:
        v = data.get(key)
        if v is not None:
            data[key] = v.replace(old, value)
        return data

    return inner


def mapping_rewriter(*args, key: str, mapping: Dict[Any, Any], is_update: bool = False, **kwargs) -> Process:
    def update_inner(data: D) -> D:
        val = data.get(key)
        if val is None:
            return data
        new_val = mapping.get(val)
        if new_val:
            data.update(new_val)
        return data

    def inner(data: D) -> D:
        val = data.get(key)
        if val is None:
            return data
        new_val = mapping.get(val)
        if new_val:
            data[key] = new_val
        return data
    if is_update:
        return update_inner
    return inner


def timestamp_rewriter(*args, key: str, fmt: str, **kwargs):
    from datetime import datetime

    def inner(data: D) -> D:
        timestamp = data.get(key)
        if timestamp is not None:
            datetime_obj = datetime.fromtimestamp(timestamp)
            data[key] = datetime_obj.strftime(fmt)

        return data
    return inner


def rename_rewriter(*args, key: str, new: str, **kwargs):
    def inner(data: D) -> D:
        data[new] = data.pop(key, None)
        return data

    return inner


def delete_rewriter(*args, keys: List[str], **kwargs):
    def inner(data: D) -> D:
        for key in keys:
            data.pop(key)
        return data

    return inner


rewriter_mapping = {k.replace('_rewriter', ''): globals(
)[k] for k in globals() if k.endswith('_rewriter')}
