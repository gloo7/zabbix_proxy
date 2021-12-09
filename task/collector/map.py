from task.const import D


def ftp_collector() -> D:
    return dict(name='luojing')


collector_mapping = {k.rstrip('_collector'): globals(
)[k] for k in globals() if k.endswith('_collector')}
