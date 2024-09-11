import scrapy


class ReadingSpiderSpider(scrapy.Spider):
    name = "reading_spider"
    start_urls = ["https://reading_spider"]

    def parse(self, response):
        pass
