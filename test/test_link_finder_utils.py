from link_finder.utils import get_all_urls


class TestLinkFinderUtils:

    html_source = """
        <html>
            <body>
            <div>
                <a href="/">Visit mohidul.xyz!</a>                                         <! -- Link: / --> 
                <a href="/products">Visit mohidul.xyz</a>                                  <! -- Link: /products --> 
                <a href="https://www.youtube.com/mohidex">Visit our youtube channel!</a>   <! -- extranal Link --> 
                <a >Visit mohidul.xyz!</a>                                                 <! -- no link --> 
                <a >Visit mohidul.xyz!</a>                                                 <! -- no link --> 
            </div>
            <div>
                <a href="/services">Visit mohidul.xyz!</a>                                 <! -- Link: /services -->
                <a href="/services/web">Visit mohidul.xyz</a>                              <! -- Link: /services/web -->
                <a href="/services/web#backend">Visit mohidul.xyz</a>                      <! -- Link: /services/web -->
                <a href="/services/web#frontent">Visit mohidul.xyz</a>                     <! -- Link: /services/web -->
                <a href="https://www.facebook.com/mohidex">Visit our facebook page!</a>    <! -- extranal Link -->
            </div>
            <div>
                <a href="/about-us">Visit mohidul.xyz</a>                                  <! -- Link: /about-us -->     
                <a href="/products/link-finder#about-finder">Visit mohidul.xyz!</a>        <! -- Link: /products/link-finder --> 
                <a href="/products/link-finder#usage">Visit mohidul.xyz!</a>               <! -- Link: /products/link-finder -->                 
                <a href="/products/link-finder#installation">Visit mohidul.xyz!</a>        <! -- Link: /products/link-finder -->                             
            </div>
            </body>
        </html>
      """

    def test_get_all_links_with_internal_url(self):
        url_list = get_all_urls(self.html_source, "https://mohidul.xyz")
        assert len(url_list) == 6

    def test_get_all_links_with_all_url(self):
        url_list = get_all_urls(self.html_source, "https://mohidul.xyz", False)
        assert len(url_list) == 8

    def test_get_all_links_with_escaping_id(self):
        url_list = get_all_urls(self.html_source, "https://mohidul.xyz")
        assert len(url_list) != 10
