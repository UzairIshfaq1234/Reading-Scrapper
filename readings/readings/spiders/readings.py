from time import strftime
from scrapy.http import Request
import scrapy
from ..items import ReadingsItem

class ExampleSpider(scrapy.Spider):
    name = "readings"
    start_urls ="https://readings.com.pk/book/1819645"

    def start_requests(self):
        yield Request(url=self.start_urls,callback=self.detail)

    def detail(self,response):
        title = response.xpath('//div[@class="card"]//div[@class="product-title"]/text()').get().replace("/n","").replace("\t","").strip()
        author_name = response.xpath('//div[@class="card"]//div[@class="author"]/a/text()').get().replace("/n","").replace("\t","").strip().title()
        print("title =",title)
        print("Author =",author_name)
        input("wait")

        item = ReadingsItem()
        item["DateExtractRun"] = strftime("%d/%m/%Y")
        item["Title"] = title
        item["AuthorName"] = author_name
        
        yield item
    

    
        
    