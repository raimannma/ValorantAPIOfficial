from typing import Dict, List, Optional

from dataclasses import dataclass

from valo_api_official.utils.init_options import InitOptions


@dataclass
class LeaderboardPlayerV1(InitOptions):
    leaderboardRank: int
    rankedRating: int
    numberOfWins: int
    competitiveTier: int
    puuid: Optional[str] = None
    gameName: Optional[str] = None
    tagLine: Optional[str] = None


@dataclass
class TierDetail(InitOptions):
    rankedRatingThreshold: int
    startingPage: int
    startingIndex: int


@dataclass
class LeaderboardV1(InitOptions):
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

    def __post_init__(self):
        self.players = [
            LeaderboardPlayerV1.from_dict(**player)
            for player in self.players
            if player is not None
        ]
        self.tierDetails = {
            tier: TierDetail.from_dict(**details)
            for tier, details in self.tierDetails.items()
        }
