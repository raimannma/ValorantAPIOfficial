from msgspec import Struct


class ActiveShardsV1(Struct):
    puuid: str
    game: str
    activeShard: str
