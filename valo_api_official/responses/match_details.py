from typing import List, Optional

from dataclasses import dataclass

from valo_api_official.utils.init_options import InitOptions


@dataclass
class MatchInfo(InitOptions):
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


@dataclass
class PlayerAbilityCasts(InitOptions):
    grenadeCasts: int
    ability1Casts: int
    ability2Casts: int
    ultimateCasts: int


@dataclass
class PlayerStats(InitOptions):
    score: int
    roundsPlayed: int
    kills: int
    deaths: int
    assists: int
    playtimeMillis: int
    abilityCasts: Optional[PlayerAbilityCasts] = None

    def __post_init__(self):
        self.abilityCasts = (
            PlayerAbilityCasts.from_dict(**self.abilityCasts)
            if self.abilityCasts is not None
            else None
        )


@dataclass
class MatchPlayers(InitOptions):
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

    def __post_init__(self):
        self.stats = PlayerStats.from_dict(**self.stats)


@dataclass
class MatchTeam(InitOptions):
    teamId: str
    won: bool
    roundsPlayed: int
    roundsWon: int
    numPoints: int


@dataclass
class Location(InitOptions):
    x: int
    y: int


@dataclass
class PlayerLocations(InitOptions):
    puuid: str
    viewRadians: float
    location: Location

    def __post_init__(self):
        self.location = Location.from_dict(**self.location)


@dataclass
class KillFinishingDamage(InitOptions):
    damageType: str
    damageItem: str
    isSecondaryFireMode: bool


@dataclass
class PlayerKills(InitOptions):
    timeSinceGameStartMillis: int
    timeSinceRoundStartMillis: int
    killer: str
    victim: str
    victimLocation: Location
    assistants: List[str]
    playerLocations: List[PlayerLocations]
    finishingDamage: KillFinishingDamage

    def __post_init__(self):
        self.victimLocation = Location.from_dict(**self.victimLocation)
        self.playerLocations = [
            PlayerLocations.from_dict(**x) for x in self.playerLocations
        ]
        self.finishingDamage = KillFinishingDamage.from_dict(**self.finishingDamage)


@dataclass
class PlayerDamage(InitOptions):
    receiver: str
    damage: int
    legshots: int
    bodyshots: int
    headshots: int


@dataclass
class PlayerEconomy(InitOptions):
    loadoutValue: int
    weapon: str
    armor: str
    remaining: int
    spent: int


@dataclass
class PlayerAbilityEffects(InitOptions):
    grenadeEffects: Optional[dict]
    ability1Effects: Optional[dict]
    ability2Effects: Optional[dict]
    ultimateEffects: Optional[dict]


@dataclass
class RoundPlayerStats(InitOptions):
    puuid: str
    kills: List[PlayerKills]
    damage: List[PlayerDamage]
    score: int
    economy: PlayerEconomy
    ability: PlayerAbilityEffects

    def __post_init__(self):
        self.kills = [PlayerKills.from_dict(**x) for x in self.kills]
        self.damage = [PlayerDamage.from_dict(**x) for x in self.damage]
        self.economy = PlayerEconomy.from_dict(**self.economy)
        self.ability = PlayerAbilityEffects.from_dict(**self.ability)


@dataclass
class MatchRoundResults(InitOptions):
    roundNum: int
    roundResult: str
    roundCeremony: str
    winningTeam: str
    bombPlanter: str
    bombDefuser: str
    plantRoundTime: int
    plantPlayerLocations: List[PlayerLocations]
    plantLocation: Location
    plantSite: str
    defuseRoundTime: int
    defusePlayerLocations: List[PlayerLocations]
    defuseLocation: Location
    playerStats: List[RoundPlayerStats]
    roundResultCode: str

    def __post_init__(self):
        self.plantPlayerLocations = [
            PlayerLocations.from_dict(**x) for x in self.plantPlayerLocations or []
        ]
        self.plantLocation = Location.from_dict(**self.plantLocation)
        self.defusePlayerLocations = [
            PlayerLocations.from_dict(**x) for x in self.defusePlayerLocations or []
        ]
        self.defuseLocation = Location.from_dict(**self.defuseLocation)
        self.playerStats = [RoundPlayerStats.from_dict(**x) for x in self.playerStats]


@dataclass
class MatchDetailsV1(InitOptions):
    matchInfo: MatchInfo
    players: List[MatchPlayers]
    coaches: List[dict]
    teams: List[MatchTeam]
    roundResults: Optional[List[MatchRoundResults]]

    def __post_init__(self):
        self.matchInfo = MatchInfo.from_dict(**self.matchInfo)
        self.players = [MatchPlayers.from_dict(**p) for p in self.players]
        self.teams = [MatchTeam.from_dict(**t) for t in self.teams]
        self.roundResults = (
            [MatchRoundResults.from_dict(**r) for r in self.roundResults]
            if self.roundResults is not None
            else None
        )
