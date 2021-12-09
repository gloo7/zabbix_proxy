from typing import Callable, Union, List

from task.config import Parser
from task.const import D
from .map import parser_mapping


def init_parser(config: Parser) -> Callable[[D], Union[D, List[D]]]:
    return parser_mapping.get(config.mode.value)(config)
