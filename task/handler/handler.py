from typing import List

from task.config import HandlerConfig
from task._typing import Handler

from .map import handler_mapping


def init_handlers(config: List[HandlerConfig] = None) -> List[Handler]:
    return [handler_mapping.get(item.mode.value)(**item.dict()) for item in config]
