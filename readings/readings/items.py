# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy # type: ignore


class ReadingsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    DateExtractRun = scrapy.Field()   
    Title = scrapy.Field()
    product_stock = scrapy.Field()


