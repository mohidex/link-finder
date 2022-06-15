#!/usr/bin/env python
#
# Copyright 2022 mohidex

"""
Python client for crawling a website.
This client library is designed to crawl a webpage and return all available links with their status.
"""
import json
from collections import deque
from typing import Dict, Iterator

import requests

from .exceptions import LinkFinderError
from .model import UrlItem
from .utils import get_all_urls, get_base_url

HTTPResponse = requests.models.Response


class LinkFinder(object):
    """
    Represents an Webpage root URL object
    """

    queue: deque = deque()
    marked: set = set()

    def __init__(
        self,
        url: str,
        depth: int = 1000,
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
        self.max_depth = depth
        self.user_agent = user_agent
        self.timeout = timeout
        self.proxies = proxies
        self.session = session or requests.Session()
        self.base_url = get_base_url(url)

    def _request(self, url: str, method: str) -> HTTPResponse:
        try:
            res = self.session.request(
                method or "GET",
                url=url,
                timeout=self.timeout,
                proxies=self.proxies,
            )
        except requests.HTTPError as e:
            error = json.loads(e.response)
            raise LinkFinderError(error)
        return res

    def start(self) -> Iterator:
        """Start the crawling process"""
        self.marked.add(self.url)
        self.queue.append((self.url, 0))
        depth: int = 0

        while self.queue:
            url, _depth = self.queue.popleft()
            if _depth > depth:
                depth += 1

            if depth > self.max_depth:
                break

            _response = self._request(url=url, method="GET")
            found_url = UrlItem(url, _response.status_code, depth)
            yield found_url

            for _url in get_all_urls(
                html_source=_response.text, base_url=self.base_url
            ):
                if _url not in self.marked:
                    self.marked.add(_url)
                    self.queue.append((_url, depth + 1))
