from typing import Any

from task._typing import D, Process


def json_parser(*args: Any, **kwargs: Any) -> Process:
    import json

    def inner(data: D) -> D:
        data.update(json.load(data.get('message')))
        return data
    return inner


def csv_parser(*args: Any, sep: str, columns: list, **kwargs: Any) -> Process:
    def inner(data: D) -> D:
        message = data.get('message')
        data.update({columns[i]: item for i, item in enumerate(message.split(sep))})
        return data
    return inner


def regex_parser(*args: Any, regex: str, **kwargs: Any) -> Process:
    import re
    cmp = re.compile(regex)

    def inner(data: D) -> D:
        message = data.get('message')
        ret = cmp.match(message)
        data.update(ret.groupdict())
        return data
    return inner


def xml_parser(*args: Any, key: str, xpath: str, **kwargs: Any) -> Process:
    from lxml import etree

    def inner(data: D) -> D:
        message = data.get('message')
        xml = etree.XML(message)
        result = xml.xpath(xpath)
        data[key] = result
        return data
    return inner


parser_mapping = {k.replace('_parser', ''): globals()[k] for k in globals() if k.endswith('_parser')}
