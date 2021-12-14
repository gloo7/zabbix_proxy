from ipaddress import IPv4Address, IPv6Address
from pathlib import Path
from typing import Dict, List, Optional, Union

from pydantic import BaseModel

from .const import CollectorChoice, HandlerChoice, ParserChoice, RewriterChoice


class CollectorConfig(BaseModel):
    mode: CollectorChoice


class LocalCollectorConfig(CollectorConfig):
    path: Path


class MysqlCollectorConfig(CollectorConfig):
    host: Union[IPv4Address, IPv6Address]
    port: int = 3306
    user: str
    password: str
    database: str
    charset: str = "utf8"


class FtpCollectorConfig(CollectorConfig):
    host: Union[IPv4Address, IPv6Address]
    port: int = 21
    user: str
    password: str
    dirname: str
    filename: str


class SSHCollectorConfig(CollectorConfig):
    host: Union[IPv4Address, IPv6Address]
    port: int = 22
    user: str
    password: str
    command: str


class ParserConfig(BaseModel):
    mode: ParserChoice
    field: str = "message"


class RegexParserConfig(ParserConfig):
    regex: str


class CsvParserConfig(ParserConfig):
    sep: str
    columns: List[str]


class XmlParserConfig(ParserConfig):
    format: str = "xml"
    key: str
    xpath: str


class RewriterConfig(BaseModel):
    mode: RewriterChoice


class SetRewriterConfig(RewriterConfig):
    key: str
    value: str


class MappingRewriterConfig(RewriterConfig):
    key: str
    mapping: Dict[str, str]


class HandlerConfig(BaseModel):
    mode: HandlerChoice


class ZabbixHandlerConfig(BaseModel):
    host: Union[IPv4Address, IPv6Address]
    port: int


class StreamHandlerConfig(HandlerConfig):
    template: str


class FileHandlerConfig(StreamHandlerConfig):
    path: Path


class Config(BaseModel):
    collector: Union[CollectorConfig, LocalCollectorConfig, MysqlCollectorConfig, FtpCollectorConfig, SSHCollectorConfig]
    parser: Optional[RegexParserConfig, CsvParserConfig, XmlParserConfig] = None
    rewrites: Optional[
        List[Union[SetRewriterConfig, MappingRewriterConfig]]] = None
    handlers: List[HandlerConfig]
