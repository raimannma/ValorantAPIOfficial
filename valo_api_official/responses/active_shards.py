from dataclasses import dataclass

from valo_api_official.utils.init_options import InitOptions


@dataclass
class ActiveShardsV1(InitOptions):
    puuid: str
    game: str
    activeShard: str
