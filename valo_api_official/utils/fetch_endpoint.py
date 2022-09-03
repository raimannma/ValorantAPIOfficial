from typing import Any, Dict, Optional

import os
import urllib.parse

import requests
from requests import Response

from valo_api_official.config import Config
from valo_api_official.exceptions.rate_limit import RateLimit


def encode_params(**kwargs) -> Dict[str, str]:
    """Returns a string of the parameters to be used in a URL.

    Args:
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        A dictionary of the parameters to be used in a URL.
    """
    out = dict()
    for key, value in kwargs.items():
        encoded_key = urllib.parse.quote_plus(str(key))
        encoded_value = urllib.parse.quote_plus(str(value))
        out[encoded_key] = encoded_value
    return out


def fetch_endpoint(
    url: str,
    query_args: Optional[Dict[str, Any]] = None,
    method: str = "GET",
    **kwargs,
) -> Response:
    """Fetches an endpoint from the API.

    Args:
        url: The endpoint definition to use.
        query_args: Any additional arguments to pass to the endpoint.
        method: The method to use when fetching the endpoint.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        A response from the API.
    """
    fetch_endpoint.session = (
        fetch_endpoint.session
        if hasattr(fetch_endpoint, "session")
        else requests.Session()
    )

    encoded_params = encode_params(**kwargs)

    # Build the URL
    # First Replace the parameters in the endpoint definition
    for key, value in encoded_params.items():
        url = url.replace(f"{{{key}}}", value)

    # Set the headers
    headers = {
        "User-Agent": Config.USER_AGENT,
        "Accept": "application/json",
    }
    if (
        "VALO_API_OFFICIAL_KEY" in os.environ
        and os.environ["VALO_API_OFFICIAL_KEY"] is not None
    ):
        headers["X-Riot-Token"] = os.environ["VALO_API_OFFICIAL_KEY"]

    # Make the request
    response = fetch_endpoint.session.request(
        method, url, params=query_args, json=query_args, headers=headers
    )
    RateLimit.limit, RateLimit.count = (
        response.headers.get("X-Method-Rate-Limit", -1),
        response.headers.get("X-Method-Rate-Limit-Count", -1),
    )

    return response
