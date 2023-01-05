from msgspec import Struct


class AccountV1(Struct):
    puuid: str
    gameName: str
    tagLine: str
