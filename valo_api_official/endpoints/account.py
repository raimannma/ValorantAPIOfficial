from valo_api_official.endpoints_config import EndpointsConfig
from valo_api_official.exceptions.valo_api_exception import ValoAPIException
from valo_api_official.responses.account import AccountV1
from valo_api_official.responses.error_response import ErrorResponse
from valo_api_official.utils.fetch_endpoint import fetch_endpoint


def get_account_by_name_v1(name: str, tag: str, **kwargs) -> AccountV1:
    """Get the account details for a player using version 1 of the endpoint.

    This is the same as
    :py:meth:`get_account_details_by_name(version="v1", name=name, tag=tag, **kwargs) <get_account_details_by_name>`

    Args:
        name: The name of the player to get the account details for.
        tag: The tag of the player to get the account details for.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        AccountV1: Account details fetched from the API.
    """
    return get_account_by_name("v1", name, tag, **kwargs)


def get_account_by_name(version: str, name: str, tag: str, **kwargs) -> AccountV1:
    """Get the account details for a player using a specific version of the endpoint.

    Args:
        version: The version of the endpoint to use.
            One of the following:
            v1 (Version 1)
        name: The name of the player to get the account details for.
        tag: The tag of the player to get the account details for.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        AccountV1: Account details fetched from the API.

    Raises:
        ValoAPIException: If the request failed.
    """
    response = fetch_endpoint(
        EndpointsConfig.ACCOUNT_BY_NAME,
        version=version,
        name=name,
        tag=tag,
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

    return AccountV1.from_dict(**response_data)


def get_account_by_puuid_v1(puuid: str, **kwargs) -> AccountV1:
    """Get the account details for a player using version 1 of the endpoint.

    This is the same as
    :py:meth:`get_account_details_by_puuid(version="v1", puuid=puuid, **kwargs) <get_account_details_by_puuid>`

    Args:
        puuid: The PUUID of the player to get the account details for.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        AccountV1: Account details fetched from the API.
    """
    return get_account_by_puuid("v1", puuid, **kwargs)


def get_account_by_puuid(version: str, puuid: str, **kwargs) -> AccountV1:
    """Get the account details for a player using a specific version of the endpoint.

    Args:
        version: The version of the endpoint to use.
            One of the following:
            v1 (Version 1)
        puuid: The PUUID of the player to get the account details for.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        AccountV1: Account details fetched from the API.

    Raises:
        ValoAPIException: If the request failed.
    """
    response = fetch_endpoint(
        EndpointsConfig.ACCOUNT_BY_PUUID,
        version=version,
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

    return AccountV1.from_dict(**response_data)
