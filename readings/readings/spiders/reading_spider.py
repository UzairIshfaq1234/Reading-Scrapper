import scrapy # type: ignore
import re

from scrapy import Request # type: ignore
from ..items import ReadingsItem
from time import strftime



class ReadingSpiderSpider(scrapy.Spider):
    name = "reading_spider"
    start_urls = "https://readings.com.pk/book/1819645"

    def start_requests(self):
        yield Request(url=self.start_urls,callback=self.reading_data)
        
    def reading_data(self,response):
        title=response.xpath('//div[@class="card"]//div[@class="product-title"]/text()').get().replace("\n","").replace("\t", "").strip()
        
        author=response.xpath('//div[@class="card"]//div[@class="author"]/a/text()').get()
        if author:
            author =author.replace("\n","").replace("\t", "").strip()
        else:
            author = "N/A"
            
        product_stock=response.xpath('//div[@class="card"]//div[@class="detail-action"]//div[@class="product-stock in-stock"]/text()').get().replace("\n","").replace("\t", "").strip()
        
        product_price=response.xpath('//div[@class="product-price listing_price"]/text()').get().replace("\n","").replace("\t", "").strip().split("£")[1]
        
        # price_number = re.search(r'[\d,.]+', product_price).group()
        category = response.xpath('//span[contains(text(),"Category")]/following-sibling::span/a/text()').get().replace("\n","").replace("\t", "").strip()
        
     
        sub_category = response.xpath('//span[contains(text(),"Sub-category:")]/following-sibling::span/a//text()').get().replace("\n","").replace("\t", "").strip()
   
        
        Additional_category = response.xpath('//span[contains(text(),"Additional Category: ")]/following-sibling::span/a//text()').get().replace("\n","").replace("\t", "").strip()


        ISBN = response.xpath('//span[contains(text(),"ISBN: ")]/following-sibling::span//text()').get().replace("\n","").replace("\t", "").strip()
        
        Shipping_Weight = response.xpath('//span[contains(text(),"Shipping Weight: ")]/following-sibling::span//text()').get().replace("\n","").replace("\t", "").strip().split(".")[1]


        descrption = response.xpath('//h2[contains(text(),"Description")]/following-sibling::p/text()').extract()#.replace("\n","").replace("\t", "").replace("<br>", "").replace("<p>", "").strip()
        descrption = "".join(descrption).replace("\n","").replace("\t", "").strip()
        print(title)
        print(author)
        print(product_stock)
        print(product_price)
        print(category)
        print(sub_category)
        print(Additional_category)
        print(ISBN)
        print(Shipping_Weight)
        print(descrption)



        
        
        input("wait")
        
        item = ReadingsItem()
        item["DateExtractRun"] = strftime("%d/%m/%Y")
        item["Title"] = title
        item["author"] = author
        item["product_stock"] = product_stock
        item["product_price"] = product_price
        item["category"] = category
        item["sub_category"] = sub_category
        item["Additional_category"] = Additional_category
        item["ISBN"] = ISBN
        item["Shipping_Weight"] = Shipping_Weight
        item["descrption"] = descrption


        
        
        yield item



