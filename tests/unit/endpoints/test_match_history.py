from typing import Optional

from uuid import UUID

import responses
from hypothesis import given, settings
from hypothesis import strategies as st

import valo_api_official
from tests.unit.endpoints.utils import get_mock_response
from valo_api_official.config import Config


@settings(deadline=None)
@given(
    version=st.sampled_from(["v1"]),
    region=st.sampled_from(Config.ALL_REGIONS),
    puuid=st.sampled_from(
        [
            "QmKHfZzxs8-CgGFkknnUsX9O5SWqZTvpXvhdud9lf1O34FnAvsxciQLxoeqg2M-jPuZsoo3myyfEjQ"
        ]
    ),
    size=st.one_of(st.none(), st.integers(min_value=1, max_value=5)),
)
@responses.activate
def test_get_match_history(version: str, region: str, puuid: UUID, size: Optional[int]):
    print(f"Test get_match_history with: {locals()}")

    puuid = str(puuid)

    url = f"https://{region}.api.riotgames.com/val/match/{version}/matchlists/by-puuid/{puuid}"

    responses.add(
        responses.GET,
        url,
        json=get_mock_response(f"match_history_{version}.json"),
        status=200,
    )

    getattr(valo_api_official, f"get_match_history_{version}")(
        region=region, puuid=puuid, size=size
    )
    assert len(responses.calls) == 1

    getattr(valo_api_official, "get_match_history")(
        version=version, region=region, puuid=puuid, size=size
    )
    assert len(responses.calls) == 2


if __name__ == "__main__":
    test_get_match_history()
