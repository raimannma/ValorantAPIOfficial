from valo_api_official.endpoints.account import (
    get_account_by_name,
    get_account_by_name_v1,
    get_account_by_puuid,
    get_account_by_puuid_v1,
)
from valo_api_official.endpoints.active_shards import (
    get_active_shards,
    get_active_shards_v1,
)
from valo_api_official.endpoints.content import get_content, get_content_v1
from valo_api_official.endpoints.leaderboard import get_leaderboard, get_leaderboard_v1
from valo_api_official.endpoints.match_details import (
    get_match_details,
    get_match_details_v1,
)
from valo_api_official.endpoints.match_history import (
    get_match_history,
    get_match_history_v1,
)
from valo_api_official.endpoints.recent_matches import (
    get_recent_matches,
    get_recent_matches_v1,
)
from valo_api_official.endpoints.status import get_status, get_status_v1

__all__ = [
    "get_account_by_name_v1",
    "get_account_by_name",
    "get_account_by_puuid_v1",
    "get_account_by_puuid",
    "get_active_shards_v1",
    "get_active_shards",
    "get_content_v1",
    "get_content",
    "get_leaderboard_v1",
    "get_leaderboard",
    "get_match_details_v1",
    "get_match_details",
    "get_match_history_v1",
    "get_match_history",
    "get_recent_matches_v1",
    "get_recent_matches",
    "get_status_v1",
    "get_status",
]
