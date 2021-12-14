from typing import Dict, Mapping, TypeVar, List, Callable


D = TypeVar('D', Dict[str, str], Mapping[str, str], List[Dict[str, str]], List[Mapping[str, str]])
Collector = Callable[[], D]
Process = Callable[[D], D]
Handler = Callable[[D], None]
