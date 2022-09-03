from dataclasses import dataclass

from valo_api_official.utils.init_options import InitOptions


@dataclass
class AccountV1(InitOptions):
    puuid: str
    gameName: str
    tagLine: str
