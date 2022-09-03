from typing import List, Optional

from dataclasses import dataclass

from valo_api_official.utils.init_options import InitOptions


@dataclass
class Error(InitOptions):
    message: Optional[str] = None
    status_code: Optional[int] = None


@dataclass
class ErrorResponse(InitOptions):
    headers: Optional[dict] = None
    error: Optional[Error] = None

    def __post_init__(self):
        self.error = Error.from_dict(**self.error) if self.error is not None else None
