from valo_api_official.endpoints_config import EndpointsConfig
from valo_api_official.exceptions.valo_api_exception import ValoAPIException
from valo_api_official.responses.error_response import ErrorResponse
from valo_api_official.responses.recent_matches import RecentMatchesV1
from valo_api_official.utils.fetch_endpoint import fetch_endpoint


def get_recent_matches_v1(region: str, queue: str, **kwargs) -> RecentMatchesV1:
    """Get recent matches for a match queue using version 1 of the endpoint.

    This is the same as
    :py:meth:`get_recent_matches(version="v1", queue=queue, **kwargs) <get_match_details>`

    Args:
        region: The region to get the recent matches for.
            One of the following:
            eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
        queue: The queue to get recent matches for.
            One of the following:
            competitive, unrated, spikerush, tournamentmode, deathmatch, onefa, ggteam
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        RecentMatchesV1: Recent matches fetched from the API.
    """
    return get_recent_matches("v1", region, queue, **kwargs)


def get_recent_matches(
    version: str, region: str, queue: str, **kwargs
) -> RecentMatchesV1:
    """Get recent matches for a match queue.

    Args:
        version: The version of the endpoint to use.
            One of the following:
            v1 (Version 1)
        region: The region to get the recent matches for.
            One of the following:
            eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
        queue: The queue to get recent matches for.
            One of the following:
            competitive, unrated, spikerush, tournamentmode, deathmatch, onefa, ggteam
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        RecentMatchesV1: Recent matches fetched from the API.

    Raises:
        ValoAPIException: If the request failed.
    """
    if region == "europe":
        region = "eu"

    response = fetch_endpoint(
        EndpointsConfig.RECENT_MATCHES,
        version=version,
        region=region,
        queue=queue,
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

    return RecentMatchesV1.from_dict(**response_data)
