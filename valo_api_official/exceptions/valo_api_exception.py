from typing import List, Optional, Union

from valo_api_official.exceptions.rate_limit import RateLimit
from valo_api_official.responses.error_response import Error, ErrorResponse


class ValoAPIException(Exception):
    """Base exception for all exceptions in the Valo API."""

    ratelimit: RateLimit

    def __init__(self, response: Union[ErrorResponse, str]):
        self.response = response
        self.ratelimit = RateLimit()
        super().__init__(response)

    def __str__(self):
        """
        Return the error message.

        Returns:
            The error message as string.
        """
        if not isinstance(self.response, ErrorResponse):
            return str(self.response)

        return self.response.error.message

    @property
    def status(self) -> Optional[str]:
        """
        Return the status code of the response.

        Returns:
            The status code of the response.
        """
        if not isinstance(self.response, ErrorResponse):
            return None
        return self.response.error.status_code

    @property
    def message(self) -> Optional[str]:
        """
        Return the error message of the response.

        Returns:
            The error message of the response.
        """
        if not isinstance(self.response, ErrorResponse):
            return None
        return self.response.error.message

    @property
    def errors(self) -> Optional[Error]:
        """
        Return the error code of the response.

        Returns:
            The error code of the response.
        """
        if not isinstance(self.response, ErrorResponse):
            return None
        return self.response.error
