# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KailiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    catalogAllName = scrapy.Field()
    commodityName = scrapy.Field()
    marketPrice = scrapy.Field()
    salePrice = scrapy.Field()
    supplierName = scrapy.Field()
