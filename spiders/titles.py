from scrapy.selector import Selector
from scrapy.spider import Spider
from scrapy.http import Request
from walk.items import WalkItem

class TitlesSpider(Spider):
    name = "titles"
    allowed_domains = ["example.com"]
    start_urls = (
        'https://www.example.com',
        )

    def parse(self, response):
	sel = Selector(response)
	for title in sel.xpath('/html/head/title/text()').extract():
	    yield WalkItem(title=title, url=response.url)
	
	for url in sel.xpath('//a/@href').extract():
	    yield Request(url, callback=self.parse)



