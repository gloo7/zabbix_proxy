from typing import Callable, List

from task.config import Rewriter
from task.const import D


def init_rewrites(config: List[Rewriter] = None) -> List[Callable[[D], D]]:
    return
