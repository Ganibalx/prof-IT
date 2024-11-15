from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetList(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Response(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class MetaData(_message.Message):
    __slots__ = ("filename",)
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    def __init__(self, filename: _Optional[str] = ...) -> None: ...

class DownloadFileResponse(_message.Message):
    __slots__ = ("file_data",)
    FILE_DATA_FIELD_NUMBER: _ClassVar[int]
    file_data: bytes
    def __init__(self, file_data: _Optional[bytes] = ...) -> None: ...

class UploadFileRequest(_message.Message):
    __slots__ = ("metadata", "file_data")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    FILE_DATA_FIELD_NUMBER: _ClassVar[int]
    metadata: MetaData
    file_data: bytes
    def __init__(self, metadata: _Optional[_Union[MetaData, _Mapping]] = ..., file_data: _Optional[bytes] = ...) -> None: ...
