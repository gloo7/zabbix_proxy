import os.path
import sys

from task._typing import D, Handler
from typing import Any, Union
from ipaddress import IPv4Address, IPv6Address
from pathlib import Path
from pyzabbix import ZabbixMetric, ZabbixSender


def zabbix_handler(*args: Any, host: Union[IPv4Address, IPv6Address], port: int, **kwargs: Any) -> Handler:
    def inner(data: D) -> None:
        hostname = data.pop('hostname', None)
        packet = [ZabbixMetric(hostname, k, v) for k, v in data.items()]
        result = ZabbixSender(zabbix_server=str(host), zabbix_port=port).send(packet)
    return inner


def stream_handler(*args: Any, template: str, **kwargs: Any) -> Handler:
    def inner(data: D) -> None:
        sys.stdout.write(template.format(**data))
    return inner


def file_handler(*args: Any, path: Path, template: str, **kwargs: Any) -> Handler:
    if not path.parent.exists():
        path.parent.mkdir(parents=True, exist_ok=True)

    def inner(data: D) -> None:
        path.write_text(template.format(**data))
    return inner


def mysql_handler(*args: Any, host: Union[IPv4Address, IPv6Address], port: int, user: str, password: str, charset: str,
                  sql: str, **kwargs) -> Handler:
    import pymysql
    conn = pymysql.connect(host=str(host), port=port, user=user, password=password, charset=charset)

    def inner(data: D) -> None:
        with conn.cursor() as cursor:
            cursor.excute(sql, tuple(data.values()))
            result = cursor.fetchone()
    return inner


handler_mapping = {k.rstrip('_handler'): globals(
)[k] for k in globals() if k.endswith('_handler')}
