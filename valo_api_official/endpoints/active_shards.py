from valo_api_official.endpoints_config import EndpointsConfig
from valo_api_official.exceptions.valo_api_exception import ValoAPIException
from valo_api_official.responses.active_shards import ActiveShardsV1
from valo_api_official.responses.error_response import ErrorResponse
from valo_api_official.utils.fetch_endpoint import fetch_endpoint


def get_active_shards_v1(puuid: str, **kwargs) -> ActiveShardsV1:
    """Get the active shards for a player using version 1 of the endpoint.

    This is the same as
    :py:meth:`get_active_shards(version="v1", puuid=puuid, **kwargs) <get_active_shards>`

    Args:
        puuid: The PUUID of the player to get the active shards for.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        ActiveShardsV1: Active Shards fetched from the API.
    """
    return get_active_shards("v1", puuid, **kwargs)


def get_active_shards(version: str, puuid: str, **kwargs) -> ActiveShardsV1:
    """Get the active shards for a player using a specific version of the endpoint.

    Args:
        version: The version of the endpoint to use.
            One of the following:
            v1 (Version 1)
        puuid: The PUUID of the player to get the active shards for.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        ActiveShardsV1: Active Shards fetched from the API.

    Raises:
        ValoAPIException: If the request failed.
    """
    response = fetch_endpoint(
        EndpointsConfig.ACTIVE_SHARDS,
        version=version,
        puuid=puuid,
        game="val",
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

    return ActiveShardsV1.from_dict(**response_data)
