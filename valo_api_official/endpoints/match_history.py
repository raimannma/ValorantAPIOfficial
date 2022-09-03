from valo_api_official.endpoints_config import EndpointsConfig
from valo_api_official.exceptions.valo_api_exception import ValoAPIException
from valo_api_official.responses.error_response import ErrorResponse
from valo_api_official.responses.match_history import MatchHistoryV1
from valo_api_official.utils.fetch_endpoint import fetch_endpoint


def get_match_history_v1(region: str, puuid: str, **kwargs) -> MatchHistoryV1:
    """Get the match history for a player using version 1 of the endpoint.

    This is the same as :py:meth:`get_match_history(version="v1", region=region, puuid=puuid, size=size,
    game_mode=game_mode, **kwargs) <get_match_history>`

    Args:
        region: The region of the player.
            One of the following:
            eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
        puuid: The puuid of the player.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        MatchHistoryV1: Match History for a player by puuid.
    """
    return get_match_history("v1", region, puuid, **kwargs)


def get_match_history(
    version: str,
    region: str,
    puuid: str,
    **kwargs,
) -> MatchHistoryV1:
    """Get the match history for a player using a specific version of the endpoint.

    Args:
        version: The version of the endpoint to use.
            One of the following:
            v1 (Version 1)
        region: The region of the player.
            One of the following:
            eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
        puuid: The puuid of the player.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        MatchHistoryV1: Match History for a player by puuid.

    Raises:
        ValoAPIException: If the request failed.
    """
    response = fetch_endpoint(
        EndpointsConfig.MATCH_HISTORY,
        version=version,
        region=region,
        puuid=puuid,
        **kwargs,
    )
    response_data = response.json()

    if response.ok is False:
        headers = dict(response.headers)
        raise ValoAPIException(
            ErrorResponse.from_dict(
                headers=headers, **{"error": response_data["status"]}
            )
        )

    return MatchHistoryV1.from_dict(**response_data)
