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
    author = scrapy.Field()
    product_stock = scrapy.Field()
    product_price = scrapy.Field()
    category = scrapy.Field()
    sub_category = scrapy.Field()
    Additional_category = scrapy.Field()
    ISBN = scrapy.Field()
    Shipping_Weight = scrapy.Field()
    descrption = scrapy.Field()



