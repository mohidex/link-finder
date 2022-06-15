# Link Finder
A python module to find the all links on a website with their status code. URLs will traverse through its child directory in Bredth's first traversal fashion. If the webpage has a lot of pages you can limit its crawling by specifying depth.

# API Guide
## `link_finder.finder` 
Provides the `LinkFinder` class.

```python
class link_finder.finder.LinkFinder(url, depth=0, user_agent="python-requests/2.25.0",
 timeout=None, proxies=None, session=None)
```
Implements the `link_finder` interface, behaving as an web-crawler while collecting all the available links exist on webpage.

## *Parameters*
- `url (str)` -  Root url of a website where the crawling process will be start.
- `depth (int)` - The maximum depth that will be allowed to crawl for any site. If not set or set `0` it will crawl all the availeble links. Defaults to `0`
- `user_agent (str)` - User-Agent to use when crawling. Defaults to `python-requests/2.25.0`
- `timeout (int)` - Waiting time for getting response. Defaults to `None`
- `proxies (dict)` - Object containing proxies for 'http' and 'https'. Defaults to `None`
- `session (request.Session)` - Session object that contains a requests interface and attribute. Defaults to `None`


## Usage

```python
>>> from link_finder.finder import LinkFinder
>>> lf = LinkFinder('https://quotes.toscrape.com/', depth=3)
<link_finder.finder.LinkFinder object at 0x7f071e5809a0>
```
### Property: ***start: Iterator***
Start the crwaling process and return a python generator of `UrlItem` class.
```python
class link_finder.model.UrlItem(url, response_status, depth)
```


#### Return type: `Iterator` 
```python
>>> process = lf.start()
>>> next(process)
UrlItem(url='https://quotes.toscrape.com/', response_status=200, depth=0)
```


## Example
```python
from link_finder.finder import LinkFinder
lf = LinkFinder('https://quotes.toscrape.com/', depth=3)
process = lf.start()
for url in process:
    print(url)
```

#### Output:
```bash
UrlItem(url='https://quotes.toscrape.com/', response_status=200, depth=0)
UrlItem(url='https://quotes.toscrape.com/tag/failure/page/1', response_status=200, depth=1)
UrlItem(url='https://quotes.toscrape.com/tag/thinking/page/1', response_status=200, depth=1)
UrlItem(url='https://quotes.toscrape.com/tag/life', response_status=200, depth=1)
.....
```

