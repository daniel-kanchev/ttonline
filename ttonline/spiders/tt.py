import scrapy


class TtSpider(scrapy.Spider):
    name = 'tt'
    allowed_domains = ['ttonline.ro']
    start_urls = ['https://ttonline.ro/stiri']

    def parse(self, response):
        pass
