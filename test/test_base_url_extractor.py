from link_finder.utils import get_base_url


class TestLinkFinderUtils:
    def test_url_with_subdomain(self):
        base_url = get_base_url("https://www.google.com/")
        assert base_url == "https://www.google.com"
        assert base_url != "https://www.google.com/"

    def test_url_with_no_subdomain(self):
        base_url = get_base_url("https://google.com/")
        assert base_url == "https://google.com"
        assert base_url != "https://google.com/"

    def test_url_with_subdomain_and_path(self):
        base_url = get_base_url("https://www.google.com/example/example1/")
        assert base_url == "https://www.google.com"
        assert base_url != "https://www.google.com/example"
        assert base_url != "https://www.google.com/example/example1"

    def test_url_with_no_subdomain_and_path(self):
        base_url = get_base_url("https://google.com/example/example1")
        assert base_url == "https://google.com"
        assert base_url != "https://google.com/example"

    def test_url_with_no_subdomain_query_param(self):
        base_url = get_base_url("https://google.com/example/?serach=example1")
        assert base_url == "https://google.com"
        assert base_url != "https://google.com/?search=example"
