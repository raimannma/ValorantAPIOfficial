import urllib.parse
from uuid import UUID

import responses
from hypothesis import given
from hypothesis import strategies as st

import valo_api_official
from tests.unit.endpoints.utils import generate_match_ids, get_mock_response
from valo_api_official.config import Config


@given(
    version=st.sampled_from(["v1"]),
    region=st.sampled_from(Config.ALL_REGIONS),
    match_id=st.sampled_from(list(generate_match_ids())),
)
@responses.activate
def test_get_match_details(version: str, region: str, match_id: UUID):
    print(f"Test get_match_details with: {locals()}")

    match_id = str(match_id)
    encoded_match_id = urllib.parse.quote_plus(match_id)

    url = f"https://{region}.api.riotgames.com/val/match/{version}/matches/{match_id}"

    responses.add(
        responses.GET,
        url,
        json=get_mock_response(f"match_details_{version}.json"),
        status=200,
    )

    getattr(valo_api_official, f"get_match_details_{version}")(
        region=region, match_id=match_id
    )
    assert len(responses.calls) == 1

    getattr(valo_api_official, "get_match_details")(
        version=version, region=region, match_id=match_id
    )
    assert len(responses.calls) == 2


if __name__ == "__main__":
    test_get_match_details()
