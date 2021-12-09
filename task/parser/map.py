from typing import Callable, Any, Union, List

from task.const import D


def json_parser(*args: Any, **kwargs: Any) -> Callable[[D], Union[D, List[D]]]:
    import json

    def inner(data: D) -> Union[D, List[D]]:
        data.update(json.load(data.get('message')))
        return data
    return inner


def csv_parser(*args: Any, sep: str, columns: list, **kwargs: Any) -> Callable[[D], Union[D, List[D]]]:
    def inner(data: D) -> Union[D, List[D]]:
        message = data.get('message')
        data.update({columns[i]: item for i, item in enumerate(message.split(sep))})
        return data
    return inner


def regex_parser(*args: Any, regex: str, **kwargs: Any) -> Callable[[D], Union[D, List[D]]]:
    import re
    cmp = re.compile(regex)

    def inner(data: D) -> Union[D, List[D]]:
        message = data.get('message')
        ret = cmp.match(message)
        data.update(ret.groupdict())
        return data
    return inner


def xml_parser(*args: Any, key: str, xpath: str, **kwargs: Any) -> Callable[[D], Union[D, List[D]]]:
    from lxml import etree

    def inner(data: D) -> Union[D, List[D]]:
        message = data.get('message')
        xml = etree.XML(message)
        result = xml.xpath(xpath)
        data[key] = result
        return data
    return inner


parser_mapping = {k.rstrip('_parser'): globals()[k] for k in globals() if k.endswith('_parser')}
