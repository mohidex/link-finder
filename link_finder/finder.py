#!/usr/bin/env python
#
# Copyright 2022 mohidex

"""
Python client for crawling a website.
This client library is designed to crawl a webpage and return all available links with their status.
"""


class LinkFinder(object):
    """
    Represents an Webpage root URL object
    """

    def __init__(
        self,
        url: str,
        depth: int = 0,
        user_agent: str = 'python-requests/2.25.0'
    ) -> None:
        """Initializes the webpage root url.
        Args:
            url: Root url of a website where the crawling process will be start.
            depth: The maximum depth that will be allowed to crawl for any site.
            user_agent: User-Agent to use when crawling
        """
        self.url = url
        self.depth = depth
        self.user_agent = user_agent
