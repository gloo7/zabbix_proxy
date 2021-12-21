import sys

from task._typing import D, Handler
from typing import Any, Union, List
from ipaddress import IPv4Address, IPv6Address
from pathlib import Path
from pyzabbix import ZabbixMetric, ZabbixSender

from logger import logger


def zabbix_handler(*args: Any, host: Union[IPv4Address, IPv6Address], port: int, **kwargs: Any) -> Handler:
    def inner(data: D) -> None:
        hostname = data.pop('hostname', None)
        packet = [ZabbixMetric(hostname, k, v) for k, v in data.items()]
        result = ZabbixSender(zabbix_server=str(host), zabbix_port=port).send(packet)
        logger.debug(result)
    return inner


def stream_handler(*args: Any, template: str, origin: bool, **kwargs: Any) -> Handler:
    def origin_inner(data: D) -> None:
        sys.stdout.write(str(data) + '\n')

    def inner(data: D) -> None:
        sys.stdout.write(template.format(**data))

    if origin:
        return origin_inner
    return inner


def file_handler(*args: Any, path: Path, template: str, origin: bool, **kwargs: Any) -> Handler:
    if not path.parent.exists():
        path.parent.mkdir(parents=True, exist_ok=True)

    def origin_inner(data: D) -> None:
        text = str(data)
        path.write_text(text + '\n')
        logger.debug(text)

    def inner(data: D) -> None:
        text = template.format(**data)
        path.write_text(text + '\n')
        logger.debug(text)

    if origin:
        return origin_inner

    return inner


def mysql_handler(*args: Any, host: Union[IPv4Address, IPv6Address], port: int, user: str, password: str, database: str,
                  charset: str, table: str, fields: List[str], **kwargs) -> Handler:
    import pymysql
    conn = pymysql.connect(host=str(host), port=port, user=user, password=password, database=database, charset=charset)
    columns = (f"`{field}`" for field in fields)
    sql = f"""INSERT INTO {table} ({", ".join(columns)}) VALUES({", ".join(("%s" for i in range(len(fields))))})"""

    def inner(data: D) -> None:
        values = [data.get(key) for key in fields]
        with conn.cursor() as cursor:
            cursor.execute(sql, values)
            logger.debug(values)
        conn.commit()
    return inner


handler_mapping = {k.replace('_handler', ''): globals(
)[k] for k in globals() if k.endswith('_handler')}
