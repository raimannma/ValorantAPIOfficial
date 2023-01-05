from typing import List

from msgspec import Struct


class RecentMatchesV1(Struct):
    currentTime: int
    matchIds: List[str]
