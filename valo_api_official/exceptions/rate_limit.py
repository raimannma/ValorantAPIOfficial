class RateLimit:
    limit: str
    """The number of requests you can make in the current period."""
    count: str
    """The number of requests you did in the current period."""

    def __str__(self) -> str:
        return f"Limit: {self.limit}; Count: {self.count}"


def rate_limit() -> RateLimit:
    """Returns the current rate limit for the API.

    Returns:
        RateLimit: A :class:`.RateLimit` object.
    """
    return RateLimit()
