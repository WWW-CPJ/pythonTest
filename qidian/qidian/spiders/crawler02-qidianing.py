import scrapy

class QidianSpider(scrapy.Spider):
    name = "qidianing"
    allowed_domains = ["qidian.com"]        # 允许爬取的域名,这个参数用于限制爬虫只能抓取指定域名下的网页内容。它可以帮助防止爬虫访问不相关或不允许的域名，确保抓取的范围在预定的域内。
    start_urls = ["https://qidian.com/free/all/"]     # 一开始爬取的URL,爬虫会从这个网址出发，开始访问和抓取网页内容。

    def parse(self, response):    # 该方法用于对response对象进行数据解析
        self.logger.info(f'Status Code: {response.status}')
 
        lis = response.xpath('//ul[@class="all-img-list cf"]/li')
        if not lis:
            self.logger.info("lis was not found")
        for li in lis:
            name = li.xpath('.//div[@class="book-mid-info"]/h2/text()').extract_first()
            if name:
                self.logger.info (name)
            else:
                print ("name was not found")
            # 如果希望得到一个字符串而不是列表，可以使用get方法，
            # name = li.xpath('./h2/text()').get(default='N/A')  # 如果没有找到，返回 'N/A'
            words = li.xpath('.//div[@class="book-mid-info"]/p[@class="update"]/span/span[@class="HVPGnCzc"]/text()').extract_first()
            chapter = li.xpath('.//div[@class="book-mid-info"]/p[@class="update"]/span/a/text()').extract_first()
            if words and chapter:
                print (words, chapter)
            else:
                print ("words and chapter was not found")

            # # 通过yield 向管道传输数据
            # dic = {
            #     'name': name,
            #     'words': words,
            #     'chapter': chapter
            # }
            # yield dic







        
