"""
utils module contains functions/methods that help to find the urls in a html source code.
"""

from typing import Optional, Set

from bs4 import BeautifulSoup


def get_all_urls(html_source: str, only_internal: Optional[bool] = True) -> Set[str]:
    """Returns all the available link in a html snippet.
    Args:
        html_source: A string containing html source.
        only_internal (optional): Boolean value to determine only internal links to return.
    """
    soup = BeautifulSoup(html_source, "html.parser")
    links: Set[str] = set()
    for atag in soup.find_all("a", href=True):
        _herf = atag["href"]
        _href_no_id = _herf.split("#")[0]
        if (only_internal and _href_no_id.startswith("/")) or not only_internal:
            links.add(_href_no_id)

    return links
