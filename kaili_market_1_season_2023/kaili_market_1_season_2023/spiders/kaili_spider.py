import scrapy


class KailiSpiderSpider(scrapy.Spider):
    name = 'kaili_spider'
    allowed_domains = ['cnncmall.com']
    start_urls = ['http://cnncmall.com/']

    def parse(self, response):
        pass
