import responses
from hypothesis import given
from hypothesis import strategies as st

import valo_api_official
from tests.unit.endpoints.utils import get_mock_response
from valo_api_official.config import Config


@given(
    version=st.sampled_from(["v1"]),
    region=st.sampled_from(Config.ALL_REGIONS),
    queue=st.sampled_from(
        [
            "competitive",
            "unrated",
            "spikerush",
            "tournamentmode",
            "deathmatch",
            "onefa",
            "ggteam",
        ]
    ),
)
@responses.activate
def test_get_recent_matches(version: str, region: str, queue: str):
    print(f"Test get_recent_matches with: {locals()}")

    url = f"https://{region}.api.riotgames.com/val/match/{version}/recent-matches/by-queue/{queue}"

    responses.add(
        responses.GET,
        url,
        json=get_mock_response(f"recent_matches_{version}.json"),
        status=200,
    )

    getattr(valo_api_official, f"get_recent_matches_{version}")(
        region=region, queue=queue
    )
    assert len(responses.calls) == 1

    getattr(valo_api_official, "get_recent_matches")(
        version=version, region=region, queue=queue
    )
    assert len(responses.calls) == 2


if __name__ == "__main__":
    test_get_recent_matches()
