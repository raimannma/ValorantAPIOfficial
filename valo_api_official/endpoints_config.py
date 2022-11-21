from valo_api_official.config import Config


class EndpointsConfig:
    ACCOUNT_BY_PUUID = (
        f"https://{Config.NEAREST_CLUSTER}.api.riotgames.com/riot/account/"
        "{version}/accounts/by-puuid/{puuid}"
    )
    ACCOUNT_BY_NAME = (
        f"https://{Config.NEAREST_CLUSTER}.api.riotgames.com/riot/account/"
        "{version}/accounts/by-riot-id/{name}/{tag}"
    )

    ACTIVE_SHARDS = (
        f"https://{Config.NEAREST_CLUSTER}.api.riotgames.com/riot/account/"
        "{version}/active-shards/by-game/{game}/by-puuid/{puuid}"
    )

    CONTENT = (
        f"https://{Config.NEAREST_CLUSTER_SHORT}.api.riotgames.com/val/content/"
        "{version}/contents"
    )

    STATUS = "https://{region}.api.riotgames.com/val/status/{version}/platform-data"
    LEADERBOARD = (
        "https://{region}.api.riotgames.com/val/ranked/{version}/leaderboards"
        "/by-act/{act_id}"
    )

    MATCH_DETAILS = (
        "https://{region}.api.riotgames.com/val/match/{version}/matches/{match_id}"
    )
    MATCH_HISTORY = "https://{region}.api.riotgames.com/val/match/{version}/matchlists/by-puuid/{puuid}"
    RECENT_MATCHES = "https://{region}.api.riotgames.com/val/match/{version}/recent-matches/by-queue/{queue}"

    RAW = "/valorant/{version}/raw"
    STORE_FEATURED = "/valorant/{version}/store-featured"
    STORE_OFFERS = "/valorant/{version}/store-offers"
    VERSION_INFO = "/valorant/{version}/version/{region}"
    WEBSITE = "/valorant/{version}/website/{countrycode}"

    MMR_DETAILS_BY_PUUID = "/valorant/{version}/by-puuid/mmr/{region}/{puuid}"
    MMR_DETAILS_BY_NAME = "/valorant/{version}/mmr/{region}/{name}/{tag}"

    MMR_HISTORY_BY_PUUID = "/valorant/{version}/by-puuid/mmr-history/{region}/{puuid}"
    MMR_HISTORY_BY_NAME = "/valorant/{version}/mmr-history/{region}/{name}/{tag}"

    CROSSHAIR = "/valorant/{version}/crosshair/generate"
