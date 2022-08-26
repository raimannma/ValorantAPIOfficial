from typing import Dict, List, Optional

from dataclasses import dataclass

from valo_api_official.utils.init_options import InitOptions


@dataclass
class Error(InitOptions):
    message: Optional[str] = None
    status_code: Optional[int] = None


@dataclass
class ErrorResponse(InitOptions):
    error: Optional[List[Error]] = None

    def __post_init__(self):
        self.errors = (
            [Error.from_dict(**e) for e in self.error]
            if self.error is not None
            else None
        )
