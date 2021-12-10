import os.path
import sys

from task.const import D
from typing import Callable, Any, Union, Tuple
from ipaddress import IPv4Address, IPv6Address
from pyzabbix import ZabbixMetric, ZabbixSender


def zabbix_handler(*args: Any, addr: Union[IPv4Address, IPv6Address], port: int, **kwargs: Any) -> Callable[[D], None]:
    def inner(data: D) -> None:
        host = data.pop('hostname', None)
        packet = [ZabbixMetric(host, k, v) for k, v in data.items()]
        result = ZabbixSender(zabbix_server=str(addr), zabbix_port=port).send(packet)
    return inner


def stream_handler(*args: Any, template: str, **kwargs: Any) -> Callable[[D], None]:
    def inner(data: D) -> None:
        sys.stdout.write(template.format(**data))
    return inner


def file_handler(*args: Any, filepath, template: str, **kwargs: Any) -> Callable[[D], None]:
    _dir = os.path.dirname(filepath)
    if not os.path.exists(_dir):
        os.mkdir(_dir)

    def inner(data: D) -> None:
        with open(filepath) as f:
            f.write(template.format(**data))
    return inner


handler_mapping = {k.rstrip('_handler'): globals(
)[k] for k in globals() if k.endswith('_handler')}
