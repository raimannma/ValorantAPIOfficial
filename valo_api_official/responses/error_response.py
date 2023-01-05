from typing import Optional

from msgspec import Struct


class Error(Struct):
    message: Optional[str] = None
    status_code: Optional[int] = None


class ErrorResponse(Struct):
    headers: Optional[dict] = None
    error: Optional[Error] = None
