import scrapy
import requests

class ProginSpider(scrapy.Spider):
    name = "progin"
    allowed_domains = ["www.proginn.com"]
    start_urls = ["https://www.proginn.com/works"]

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",

    }

    def parse(self, response):
        response = requests.get(self.start_urls[0], headers=self.headers)
        
        

