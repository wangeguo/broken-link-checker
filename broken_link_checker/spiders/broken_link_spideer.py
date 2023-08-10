import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from broken_link_checker.items import BrokenLinkCheckerItem

class BrokenLinkSpider(CrawlSpider):
    name = "broken_link_spider"
    handle_httpstatus_list = [404]
    allowed_domains = []
    start_urls = []

    def __init__(self, domain=None, url=None, *args, **kwargs):
        super(BrokenLinkSpider, self).__init__(*args, **kwargs)
        if domain:
            self.allowed_domains = [domain]
        if url:
            self.start_urls = [url]

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        if response.status != 200:  # Check if status code is not 200 OK
            item = BrokenLinkCheckerItem()
            item['url'] = response.url
            item['status'] = response.status
            item['referer'] = response.request.headers.get('Referer')
            yield item
