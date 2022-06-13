from dataclasses import dataclass


@dataclass
class UrlItem:
    """Class for describe a URL item."""

    url: str
    response_status: int
    depth: int
