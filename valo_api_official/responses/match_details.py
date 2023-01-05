from typing import List, Optional

from msgspec import Struct


class MatchInfo(Struct):
    matchId: str
    mapId: str
    gameVersion: str
    gameLengthMillis: int
    gameStartMillis: int
    isCompleted: bool
    customGameName: str
    gameMode: str
    isRanked: bool
    seasonId: str
    queueId: Optional[str] = None
    provisioningFlowID: Optional[str] = None


class PlayerAbilityCasts(Struct):
    grenadeCasts: int
    ability1Casts: int
    ability2Casts: int
    ultimateCasts: int


class PlayerStats(Struct):
    score: int
    roundsPlayed: int
    kills: int
    deaths: int
    assists: int
    playtimeMillis: int
    abilityCasts: Optional[PlayerAbilityCasts] = None


class MatchPlayers(Struct):
    puuid: str
    gameName: str
    tagLine: str
    teamId: str
    partyId: str
    characterId: str
    stats: PlayerStats
    competitiveTier: int
    playerCard: str
    playerTitle: str


class MatchTeam(Struct):
    teamId: str
    won: bool
    roundsPlayed: int
    roundsWon: int
    numPoints: int


class Location(Struct):
    x: int
    y: int


class PlayerLocations(Struct):
    puuid: str
    viewRadians: float
    location: Location


class KillFinishingDamage(Struct):
    damageType: str
    damageItem: str
    isSecondaryFireMode: bool


class PlayerKills(Struct):
    timeSinceGameStartMillis: int
    timeSinceRoundStartMillis: int
    killer: str
    victim: str
    victimLocation: Location
    assistants: List[str]
    playerLocations: List[PlayerLocations]
    finishingDamage: KillFinishingDamage


class PlayerDamage(Struct):
    receiver: str
    damage: int
    legshots: int
    bodyshots: int
    headshots: int


class PlayerEconomy(Struct):
    loadoutValue: int
    weapon: str
    armor: str
    remaining: int
    spent: int


class PlayerAbilityEffects(Struct):
    grenadeEffects: Optional[dict]
    ability1Effects: Optional[dict]
    ability2Effects: Optional[dict]
    ultimateEffects: Optional[dict]


class RoundPlayerStats(Struct):
    puuid: str
    kills: List[PlayerKills]
    damage: List[PlayerDamage]
    score: int
    economy: PlayerEconomy
    ability: PlayerAbilityEffects


class MatchRoundResults(Struct):
    roundNum: int
    roundResult: str
    roundCeremony: str
    winningTeam: str
    plantRoundTime: int
    plantLocation: Location
    plantSite: str
    defuseRoundTime: int
    defuseLocation: Location
    playerStats: List[RoundPlayerStats]
    roundResultCode: str
    bombPlanter: Optional[str] = None
    bombDefuser: Optional[str] = None
    plantPlayerLocations: Optional[List[PlayerLocations]] = None
    defusePlayerLocations: Optional[List[PlayerLocations]] = None


class MatchDetailsV1(Struct):
    matchInfo: MatchInfo
    players: List[MatchPlayers]
    coaches: List[dict]
    teams: List[MatchTeam]
    roundResults: Optional[List[MatchRoundResults]]
