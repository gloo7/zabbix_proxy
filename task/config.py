from ipaddress import IPv4Address, IPv6Address
from pathlib import Path
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
    key: str
    mapping: Dict[str, str]


class Handler(BaseModel):
    mode: HandlerChoice


class ZabbixHandler(BaseModel):
    addr: Union[IPv4Address, IPv6Address]
    port: int


class StreamHandler(Handler):
    template: str


class FileHandler(StreamHandler):
    filepath: Path


class Config(BaseModel):
    collector: Collector
    parser: Union[RegexParser, CsvParser, XmlParser]
    rewrites: Optional[
        List[Union[SetRewriter, MappingRewriter]]] = None
    handlers: List[Handler]
