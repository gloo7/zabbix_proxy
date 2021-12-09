from task.const import D


def zabbix_handler(data: D) -> None:
    print(data)
    return None


handler_mapping = {k.rstrip('_handler'): globals(
)[k] for k in globals() if k.endswith('_handler')}
