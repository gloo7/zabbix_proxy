from typing import Dict, List, Optional, Union
from pydantic import BaseModel

from .const import CollectorChoice, HandlerChoice, ParserChoice, RewriterChoice


class Collector(BaseModel):
    mode: CollectorChoice


class Parser(BaseModel):
    mode: ParserChoice


class RegexParser(Parser):
    regex: str


class CsvParser(Parser):
    sep: str
    columns: List[str]


class XmlParser(Parser):
    format: str = 'xml'
    key: str
    xpath: str


class Rewriter(BaseModel):
    mode: RewriterChoice


class SetRewriter(Rewriter):
    key: str
    value: str


class MappingRewriter(Rewriter):
    map: Dict[str, str]


class Handler(BaseModel):
    mode: HandlerChoice
    ip: str


class Config(BaseModel):
    collector: Collector
    parser: Union[RegexParser, CsvParser, XmlParser]
    rewrites: Optional[
        List[Union[SetRewriter, MappingRewriter]]] = None
    handlers: List[Handler]


if __name__ == '__main__':
    try:
        config = Config.parse_file(path='./config.json')
    except Exception as e:
        print(e)
