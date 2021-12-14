from typing import Callable

from task.config import CollectorConfig
from task._typing import Collector

from .map import collector_mapping


def init_collector(config: CollectorConfig) -> Collector:
    return collector_mapping.get(config.mode.value)(**config.dict())
