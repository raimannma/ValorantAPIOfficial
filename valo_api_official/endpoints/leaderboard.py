from typing import Optional

from valo_api_official.endpoints_config import EndpointsConfig
from valo_api_official.exceptions.valo_api_exception import ValoAPIException
from valo_api_official.responses.error_response import ErrorResponse
from valo_api_official.responses.leaderboard import LeaderboardV1
from valo_api_official.utils.fetch_endpoint import fetch_endpoint


def get_leaderboard_v1(
    region: str,
    act_id: Optional[str] = None,
    start: Optional[int] = None,
    size: Optional[int] = None,
    **kwargs,
) -> LeaderboardV1:
    """Get the leaderboard for a region using version 1 of the endpoint.

    This is the same as
    :py:meth:`get_leaderboard(version="v1", region=region, puuid=puuid, name=name, tag=tag, **kwargs) <get_leaderboard>`

    You can also filter by puuid or name and tag.

    Args:
        region: The region to get the leaderboard for.
            One of the following:
            eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
        act_id: The season ID to get the leaderboard for.
        start: The start index of the leaderboard. Can be used for pagination.
        size: The size of the leaderboard.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        LeaderboardV1: The leaderboard for the region.
    """
    return get_leaderboard("v1", region, act_id, start, size, **kwargs)


def get_leaderboard(
    version: str,
    region: str,
    act_id: Optional[str] = None,
    start: Optional[int] = None,
    size: Optional[int] = None,
    **kwargs,
) -> LeaderboardV1:
    """Get the leaderboard for a region using a specific version of the endpoint.

    You can also filter by puuid or name and tag if you are using v1.

    Args:
        version: The version of the endpoint. One of the following:
            v1 (Version 1)
        region: The region to get the leaderboard for.
            One of the following:
            eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
        act_id: The act ID to get the leaderboard for.
        start: The start index of the leaderboard. Can be used for pagination.
        size: The size of the leaderboard.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        LeaderboardV1: The leaderboard for the region.

    Raises:
        ValoAPIException: If the request failed.
    """
    query_args = dict()
    if start is not None:
        query_args["startIndex"] = start
    if size is not None:
        query_args["size"] = size

    if region == "europe":
        region = "eu"

    response = fetch_endpoint(
        EndpointsConfig.LEADERBOARD,
        region=region,
        version=version,
        act_id=act_id,
        query_args=query_args,
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

    return LeaderboardV1.from_dict(**response_data)
