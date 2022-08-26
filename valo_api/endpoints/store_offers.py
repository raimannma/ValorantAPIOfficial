from valo_api.endpoints_config import EndpointsConfig
from valo_api.exceptions.valo_api_exception import ValoAPIException
from valo_api.responses.error_response import ErrorResponse
from valo_api.responses.store_offers import StoreOffersV1
from valo_api.utils.fetch_endpoint import fetch_endpoint


def get_store_offers_v1(**kwargs) -> StoreOffersV1:
    """Get the store offers using version 1 of the endpoint.

    This is the same as
    :py:meth:`get_store_offers(version="v1", **kwargs) <get_store_offers>`

    Args:
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        StoreOffersV1: Store Offers fetched from the API.
    """
    return get_store_offers("v1", **kwargs)


def get_store_offers(version: str, **kwargs) -> StoreOffersV1:
    """Get the store offers using a specific version of the endpoint.

    Args:
        version: The version of the endpoint to use.
            One of the following:
            v1 (Version 1)
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        StoreOffersV1: Store Offers fetched from the API.

    Raises:
        ValoAPIException: If the request failed.
    """
    response = fetch_endpoint(
        EndpointsConfig.STORE_OFFERS,
        version=version,
        **kwargs,
    )
    response_data = response.json()

    if response.ok is False:
        headers = dict(response.headers)
        raise ValoAPIException(
            ErrorResponse.from_dict(headers=headers, **response_data)
        )

    return StoreOffersV1.from_dict(**response_data["data"])
