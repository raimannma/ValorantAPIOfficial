from typing import Dict, List, Optional

from msgspec import Struct


class LeaderboardPlayerV1(Struct):
    leaderboardRank: int
    rankedRating: int
    numberOfWins: int
    competitiveTier: int
    puuid: Optional[str] = None
    gameName: Optional[str] = None
    tagLine: Optional[str] = None


class TierDetail(Struct):
    rankedRatingThreshold: int
    startingPage: int
    startingIndex: int


class LeaderboardV1(Struct):
    actId: str
    players: List[LeaderboardPlayerV1]
    totalPlayers: int
    immortalStartingPage: int
    immortalStartingIndex: int
    topTierRRThreshold: int
    tierDetails: Dict[int, TierDetail]
    startIndex: int
    query: str
    shard: str
