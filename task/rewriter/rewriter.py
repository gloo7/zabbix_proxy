from typing import Callable, List

from task.config import RewriterConfig
from task._typing import Process

from .map import rewriter_mapping


def init_rewrites(config: List[RewriterConfig] = None) -> List[Process]:
    return [rewriter_mapping.get(item.mode)(**item.dict()) for item in config]
