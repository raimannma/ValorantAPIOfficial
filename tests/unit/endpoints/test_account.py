import urllib.parse

import pytest
import responses
from hypothesis import given
from hypothesis import strategies as st
from responses import matchers

import valo_api_official
from tests.unit.endpoints.utils import get_mock_response
from valo_api_official.config import Config
from valo_api_official.exceptions.valo_api_exception import ValoAPIException


@given(
    version=st.sampled_from(["v1"]),
    name=st.text(min_size=2),
    tag=st.text(min_size=2),
)
@responses.activate
def test_get_account_by_name(version: str, name: str, tag: str):
    print(f"Test get_account_by_name with: {locals()}")

    encoded_name = urllib.parse.quote_plus(name).lower()
    encoded_tag = urllib.parse.quote_plus(tag).lower()

    url = f"https://{Config.NEAREST_CLUSTER}.api.riotgames.com/riot/account/{version}/accounts/by-riot-id/{encoded_name}/{encoded_tag}"

    responses.add(
        responses.GET,
        url,
        json=get_mock_response(f"account_{version}.json"),
        status=200,
    )

    getattr(valo_api_official, f"get_account_by_name_{version}")(name=name, tag=tag)
    assert len(responses.calls) == 1

    getattr(valo_api_official, "get_account_by_name")(
        version=version, name=name, tag=tag
    )
    assert len(responses.calls) == 2


if __name__ == "__main__":
    test_get_account_by_name()
