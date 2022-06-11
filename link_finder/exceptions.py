"""
The exceptions module contains Exception subclasses whose instances might be
raised by the sdk.
"""

from typing import Any


class LinkFinderError(Exception):
    """Encapsulates an http execption from LinkFinder."""

    def __init__(self, result: Any) -> None:
        self.result = result
        self.code = None
        self.error_subcode = None

        try:
            self.type = result["error_code"]
        except (KeyError, TypeError):
            self.type = ""

        # OAuth 2.0 Draft 10
        try:
            self.message = result["error_description"]
        except (KeyError, TypeError):
            # OAuth 2.0 Draft 00
            try:
                self.message = result["error"]["message"]
                self.code = result["error"].get("code")
                self.error_subcode = result["error"].get("error_subcode")
                if not self.type:
                    self.type = result["error"].get("type", "")
            except (KeyError, TypeError):
                # REST server style
                try:
                    self.message = result["error_msg"]
                except (KeyError, TypeError):
                    self.message = result

        Exception.__init__(self, self.message)
