import urllib.parse

import responses
from hypothesis import given
from hypothesis import strategies as st

import valo_api_official
from tests.unit.endpoints.utils import get_mock_response
from valo_api_official.config import Config


@given(
    version=st.sampled_from(["v1"]),
    puuid=st.sampled_from(
        [
            "QmKHfZzxs8-CgGFkknnUsX9O5SWqZTvpXvhdud9lf1O34FnAvsxciQLxoeqg2M-jPuZsoo3myyfEjQ"
        ]
    ),
)
@responses.activate
def test_get_active_shards(version: str, puuid: str):
    print(f"Test test_get_active_shards with: {locals()}")

    encoded_puuid = urllib.parse.quote_plus(puuid)

    url = f"https://{Config.NEAREST_CLUSTER}.api.riotgames.com/riot/account/{version}/active-shards/by-game/val/by-puuid/{encoded_puuid}"

    responses.add(
        responses.GET,
        url,
        json=get_mock_response(f"active_shards_{version}.json"),
        status=200,
    )

    getattr(valo_api_official, f"get_active_shards_{version}")(puuid=puuid)
    assert len(responses.calls) == 1

    getattr(valo_api_official, "get_active_shards")(version=version, puuid=puuid)
    assert len(responses.calls) == 2


if __name__ == "__main__":
    test_get_active_shards()
