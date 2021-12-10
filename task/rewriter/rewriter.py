from typing import Callable, List

from task.config import Rewriter
from task.const import D

from .map import rewriter_mapping


def init_rewrites(config: List[Rewriter] = None) -> List[Callable[[D], D]]:
    return [rewriter_mapping.get(config_item.mode) for config_item in config]
