from typing import List

from dataclasses import dataclass

from valo_api_official.utils.init_options import InitOptions


@dataclass
class MatchRaw(InitOptions):
    matchId: str
    gameStartTimeMillis: int
    queueId: str


@dataclass
class MatchHistoryV1(InitOptions):
    puuid: str
    history: List[MatchRaw]

    def __post_init__(self):
        self.history = [MatchRaw.from_dict(**h) for h in self.history]
