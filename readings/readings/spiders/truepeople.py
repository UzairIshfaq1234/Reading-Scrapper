import scrapy # type: ignore
import re

from scrapy import Request # type: ignore
from ..items import ReadingsItem
from time import strftime

class TruepeopleSpider(scrapy.Spider):
    name = "TruepeopleSpider"
    start_urls = "https://www.truepeoplesearch.com/"

    def start_requests(self):
        yield Request(url=self.start_urls,callback=self.true_data)
        
    def true_data(self,response):
        title=response.xpath('//h5[@class="card-header text-center"]/text()').get().replace("/n","").replace("\t", "").strip()
               
               
        print(title)
