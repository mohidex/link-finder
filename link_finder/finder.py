#!/usr/bin/env python
#
# Copyright 2022 mohidex

"""
Python client for crawling a website.
This client library is designed to crawl a webpage and return all available links with their status.
"""
import json
from typing import Dict

import requests

from .exceptions import LinkFinderError

HTTPResponse = requests.models.Response


class LinkFinder(object):
    """
    Represents an Webpage root URL object
    """

    def __init__(
        self,
        url: str,
        depth: int = 0,
        user_agent: str = "python-requests/2.25.0",
        timeout: int = None,
        proxies: Dict[str, str] = None,
        session: requests.Session = None,
    ) -> None:
        """Initializes the webpage root url.
        Args:
            url: Root url of a website where the crawling process will be start.
            depth: The maximum depth that will be allowed to crawl for any site.
            user_agent: User-Agent to use when crawling
            timeout: waiting time for getting response
            proxies: Object containing proxies for 'http' and 'https'
            session: Session object that contains a requests interface and attribute
        """
        self.url = url
        self.depth = depth
        self.user_agent = user_agent
        self.timeout = timeout
        self.proxies = proxies
        self.session = session or requests.Session()

    def _request(self, url: str, method: str) -> HTTPResponse:
        try:
            response = self.session.request(
                method or "GET",
                url=url,
                timeout=self.timeout,
                proxies=self.proxies,
            )
        except requests.HTTPError as e:
            response = json.loads(e.response)
            raise LinkFinderError(response)
        return response

    def start(self) -> None:
        """Start the crawling process"""
        pass
