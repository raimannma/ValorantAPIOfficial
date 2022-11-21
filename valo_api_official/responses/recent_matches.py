from typing import List

from dataclasses import dataclass

from valo_api_official.utils.init_options import InitOptions


@dataclass
class RecentMatchesV1(InitOptions):
    currentTime: int
    matchIds: List[str]
