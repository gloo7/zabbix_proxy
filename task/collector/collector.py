from typing import Callable

from task.config import Collector
from task.const import D

from .map import collector_mapping


def init_collector(config: Collector) -> Callable[[], D]:
    return collector_mapping.get(config.mode.value)

