from typing import List

from msgspec import Struct


class MatchRaw(Struct):
    matchId: str
    gameStartTimeMillis: int
    queueId: str


class MatchHistoryV1(Struct):
    puuid: str
    history: List[MatchRaw]
