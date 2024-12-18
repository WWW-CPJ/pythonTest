import scrapy


class DocqhomeSpider(scrapy.Spider):
    name = "docqHome"
    allowed_domains = ["www.doupocangqiong.org"]
    start_urls = ["https://www.doupocangqiong.org/doupocangqiong/"]

    def parse(self, response):
        pass
