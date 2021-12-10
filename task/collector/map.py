from task.const import D


def local_collector() -> D:
    return dict(message='')


def ftp_collector() -> D:
    return dict(message='')


def db_collector() -> D:
    return dict(message='')


def ssh_collector() -> D:
    return dict(message='')


collector_mapping = {k.rstrip('_collector'): globals(
)[k] for k in globals() if k.endswith('_collector')}
