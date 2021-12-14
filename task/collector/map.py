import sys
from ipaddress import IPv4Address, IPv6Address
from pathlib import Path
from typing import Callable, Union

from logger import logger
from task._typing import D, Collector


def local_collector(*args, path: Path, **kwargs) -> Collector:
    if not path.exists():
        logger.error(f'{path} is not exists.')
        sys.exit(1)

    def inner() -> D:
        return dict(message=path.read_text())
    return inner


def ftp_collector(*args, host: Union[IPv4Address, IPv6Address], port: int, user: str, password: str, dirname: str,
                  filename: str, **kwargs) -> Collector:
    from ftplib import FTP
    ftp = FTP()
    ftp.set_debuglevel(2)
    ftp.connect(str(host), port)
    ftp.login(user, password)
    ftp.cwd(dirname)

    def inner() -> D:
        with open(filename, 'r') as f:
            message = f.read()

        ftp.quit()
        return dict(message=message, host=host)
    return inner


def mysql_collector(*args, host: Union[IPv4Address, IPv6Address], port: int, user: str, password: str, charset: str,
                    sql: str, **kwargs) -> Collector:
    import pymysql
    conn = pymysql.connect(host=str(host), port=port,
                           user=user, password=password, charset=charset)

    def inner() -> D:
        with conn.cursor() as cursor:
            cursor.excute(sql)
            result = cursor.fetchone()
        return result.update({
            'message': '',
            'host': host,
        })
    return inner


def ssh_collector(*args, host: Union[IPv4Address, IPv6Address], port: int, user: str, password: str, command: str,
                  **kwargs) -> Collector:
    import paramiko
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(str(host), port, user, password, timeout=10)

    def inner() -> D:
        stdin, stdout, stderr = ssh.exec_command(command)
        result = str(stdout.read())
        ssh.close()
        return dict(message=result)
    return inner


collector_mapping = {k.rstrip('_collector'): globals(
)[k] for k in globals() if k.endswith('_collector')}
