import pytest
import responses
from hypothesis import given
from hypothesis import strategies as st

import valo_api
from tests.unit.endpoints.utils import (
    get_error_responses,
    get_mock_response,
    validate_exception,
)
from valo_api.config import Config
from valo_api.exceptions.valo_api_exception import ValoAPIException


@given(version=st.sampled_from(["v1"]))
@responses.activate
def test_get_store_offers(version: str):
    print(f"Test get_store_offers with: {locals()}")

    url = f"{Config.BASE_URL}/valorant/{version}/store-offers"

    responses.add(
        responses.GET,
        url,
        json=get_mock_response(f"store_offers_{version}.json"),
        status=200,
    )

    getattr(valo_api, f"get_store_offers_{version}")()
    assert len(responses.calls) == 1

    getattr(valo_api, "get_store_offers")(version=version)
    assert len(responses.calls) == 2


@given(
    version=st.sampled_from(["v1"]),
    error_response=st.sampled_from(get_error_responses("store_offers")),
)
@responses.activate
def test_get_store_offers_error(version: str, error_response: dict):
    print(f"Test get_store_offers_error with: {locals()}")

    url = f"{Config.BASE_URL}/valorant/{version}/store-offers"

    responses.add(
        responses.GET,
        url,
        json=error_response,
        status=int(error_response["status"]) if "status" in error_response else 500,
    )

    with pytest.raises(ValoAPIException) as excinfo:
        getattr(valo_api, f"get_store_offers_{version}")()
    assert len(responses.calls) == 1
    validate_exception(error_response, excinfo)

    with pytest.raises(ValoAPIException) as excinfo:
        getattr(valo_api, "get_store_offers")(version=version)
    assert len(responses.calls) == 2
    validate_exception(error_response, excinfo)


if __name__ == "__main__":
    test_get_store_offers()
    test_get_store_offers_error()
