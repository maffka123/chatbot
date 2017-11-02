import scrapy
from scrapy.selector import Selector 
from scrapy.http import HtmlResponse
from scrapy.http.request import Request

class BrickSetSpider(scrapy.Spider):
    name = "Phrase_spider"
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
    start_urls = ['http://www.gutenberg.org/cache/epub/19719/pg19719.html']
    def make_requests_from_url(self, url):
        return Request(url, dont_filter=True, meta = {'dont_redirect': True},
                       callback=self.parse)
    def parse(self, response):
    	    #response.xpath('.//p[@id = "lid00031"]/text()').extract() 
    	    #response.xpath('//h5/text()').extract() 
    	    yield {
                'name': response.xpath('.//p[@id = "lid00031"]/text()').extract()
                }


