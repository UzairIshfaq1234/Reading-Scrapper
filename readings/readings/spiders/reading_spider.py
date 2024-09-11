import scrapy

from scrapy import Request

class ReadingSpiderSpider(scrapy.Spider):
    name = "reading_spider"
    start_urls = "https://readings.com.pk/book/1819645"

    def start_requests(self):
        yield Request(url=self.start_urls,callback=self.reading_data)
        
    def reading_data(self,response):
        title=response.xpath('//div[@class="card"]//div[@class="product-title"]/text()').get().replace("/n","").replace("\t", "").strip()
        
        author=response.xpath('//div[@class="card"]//div[@class="author"]/a/text()').get().replace("/n","").replace("\t", "").strip()
        
        product_stock=response.xpath('//div[@class="card"]//div[@class="detail-action"]//div[@class="product-stock in-stock"]/text()').get().replace("/n","").replace("\t", "").strip()
        
        product_price=response.xpath('//div[@class="card"]//div[@class="detail-action"]//div[@class="product-stock in-stock"]/text()').get().replace("/n","").replace("\t", "").strip()
        
        
        
        
        print(title)
        print(author)
        print(product_stock)
        print(product_price)


