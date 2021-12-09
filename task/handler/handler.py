from typing import Callable, List

from task.config import Handler
from task.const import D

from .map import handler_mapping


def init_handlers(config: List[Handler] = None) -> List[Callable[[D], D]]:
    return [handler_mapping.get(item.mode.value)(item) for item in config]
