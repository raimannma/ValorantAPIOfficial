import urllib.parse

import responses
from hypothesis import given, settings
from hypothesis import strategies as st

import valo_api_official
from tests.unit.endpoints.utils import generate_act_ids, get_mock_response
from valo_api_official.config import Config


@settings(deadline=None)
@given(
    version=st.sampled_from(["v1"]),
    region=st.sampled_from(Config.ALL_REGIONS),
    act_id=st.sampled_from(list(generate_act_ids())),
)
@responses.activate
def test_get_leaderboard(version: str, region: str, act_id: str):
    print(f"Test get_leaderboard with: {locals()}")

    encoded_region = urllib.parse.quote_plus(region).lower()

    url = f"https://{region}.api.riotgames.com/val/ranked/{version}/leaderboards/by-act/{act_id}"

    responses.add(
        responses.GET,
        url,
        json=get_mock_response(f"leaderboard_{version}.json"),
        status=200,
    )

    getattr(valo_api_official, f"get_leaderboard_{version}")(
        region=region, act_id=act_id
    )
    assert len(responses.calls) == 1

    getattr(valo_api_official, "get_leaderboard")(
        version=version, region=region, act_id=act_id
    )
    assert len(responses.calls) == 2


if __name__ == "__main__":
    test_get_leaderboard()
