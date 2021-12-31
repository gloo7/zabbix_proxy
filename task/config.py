from ipaddress import IPv4Address, IPv6Address
from pathlib import Path
from typing import Dict, List, Optional, Union, Any

from pydantic import BaseModel

from .const import CollectorChoice, HandlerChoice, ParserChoice, RewriterChoice, FileMatchChoice, MethodChoice


class CollectorConfig(BaseModel):
    mode: CollectorChoice


class FileCollectorConfig(CollectorConfig):
    dir: Path
    filename: str
    file_match: FileMatchChoice = FileMatchChoice.strict


class MysqlCollectorConfig(CollectorConfig):
    host: Union[IPv4Address, IPv6Address]
    port: int = 3306
    user: str
    password: str
    database: str
    charset: str = "utf8"
    fields: List[str]
    table: str


class FtpCollectorConfig(FileCollectorConfig):
    host: Union[IPv4Address, IPv6Address]
    port: int = 21
    user: str
    password: str


class APICollectorConfig(CollectorConfig):
    url: str
    method: MethodChoice
    data: Optional[dict] = None
    json_data: Optional[dict] = None
    headers: Optional[dict] = None
    index: Optional[str] = None


class CMDCollectorConfig(CollectorConfig):
    command: str


class SSHCollectorConfig(CMDCollectorConfig):
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
    key: str
    mode: RewriterChoice


class SetRewriterConfig(RewriterConfig):
    value: str


class MappingRewriterConfig(RewriterConfig):
    mapping: Dict[Any, Any]
    is_update: bool


class TimestampRewriterConfig(RewriterConfig):
    fmt: str = '%Y-%m-%d %H:%M:%S'


class RenameRewriterConfig(RewriterConfig):
    new: str


class DeleteRewriterConfig(RewriterConfig):
    keys: List[str]


class HandlerConfig(BaseModel):
    mode: HandlerChoice


class ZabbixHandlerConfig(BaseModel):
    host: Union[IPv4Address, IPv6Address]
    port: int


class StreamHandlerConfig(HandlerConfig):
    origin: Optional[bool] = False
    template: Optional[str] = '{message}'


class MysqlHandlerConfig(HandlerConfig):
    host: Union[IPv4Address, IPv6Address]
    port: int = 3306
    user: str
    password: str
    database: str
    charset: str = "utf8mb4"
    fields: List[str]
    table: str


class FileHandlerConfig(StreamHandlerConfig):
    path: Path


class Config(BaseModel):
    collector: Union[MysqlCollectorConfig, FtpCollectorConfig, SSHCollectorConfig, APICollectorConfig,
                     FileCollectorConfig, CMDCollectorConfig]
    parser: Union[RegexParserConfig, CsvParserConfig, XmlParserConfig] = None
    rewriters: Optional[List[Union[SetRewriterConfig, MappingRewriterConfig, RenameRewriterConfig, DeleteRewriterConfig,
                                   TimestampRewriterConfig]]] = None
    handlers: List[Union[MysqlHandlerConfig, FileHandlerConfig, StreamHandlerConfig]]
