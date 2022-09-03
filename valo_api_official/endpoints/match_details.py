from valo_api_official.endpoints_config import EndpointsConfig
from valo_api_official.exceptions.valo_api_exception import ValoAPIException
from valo_api_official.responses.error_response import ErrorResponse
from valo_api_official.responses.match_details import MatchDetailsV1
from valo_api_official.utils.fetch_endpoint import fetch_endpoint


def get_match_details_v1(region: str, match_id: str, **kwargs) -> MatchDetailsV1:
    """Get the match details for a match using version 1 of the endpoint.

    This is the same as
    :py:meth:`get_match_details(version="v1", matchId=matchId, **kwargs) <get_match_details>`

    Args:
        region: The region to get the leaderboard for.
            One of the following:
            eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
        match_id: The match ID to get the details for.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        MatchDetailsV1: Match details fetched from the API.
    """
    return get_match_details("v1", region, match_id, **kwargs)


def get_match_details(
    version: str, region: str, match_id: str, **kwargs
) -> MatchDetailsV1:
    """Get the match details for a match using a specific version of the endpoint.

    Args:
        version: The version of the endpoint to use.
            One of the following:
            v1 (Version 1)
        region: The region to get the leaderboard for.
            One of the following:
            eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
        match_id: The match ID to get the details for.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        MatchDetailsV1: Match details fetched from the API.

    Raises:
        ValoAPIException: If the request failed.
    """
    if region == "europe":
        region = "eu"

    response = fetch_endpoint(
        EndpointsConfig.MATCH_DETAILS,
        version=version,
        region=region,
        match_id=match_id,
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

    return MatchDetailsV1.from_dict(**response_data)
