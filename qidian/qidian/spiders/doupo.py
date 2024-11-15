import scrapy


class DoupoSpider(scrapy.Spider):
    name = "doupo"
    allowed_domains = ["doupocangqiong.org"]
    start_urls = ["https://www.doupocangqiong.org/doupocangqiong/"]

    def parse(self, response):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
        }
        for url in self.start_urls:
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)

        status_code = response.status
        print (status_code)

        # 测试用例，输出第一章 名字
        name = response.xpath('/html/body/metaname="description"/div/div[2]/div[1]/div[1]/div[2]/h1/text()').get()
        print (name)
        author = response.xpath('/html/body/metaname="description"/div/div[2]/div[1]/div[1]/div[2]/span[1]/text()').get()
        print (author)
        description = response.xpath('/html/body/metaname="description"/div/div[2]/div[1]/div[1]/p/text()').get()
        print (description)


        # lis = response.xpath('//*[@id="play_0"]/ul/li')
        # for li in lis:
        #     li = response.xpath('.//li/a/text()').get
        #     if li:
        #         print(li)
        #     else:
        #         print ("it has error")
        # # 输出格式：  <Selector query='.//li/a/text()' data='第一千六百二十章  斗帝强者的力量！'>,

        lis = response.xpath('//*[@id="play_0"]/ul/li/a/text()').getall()
        for li in lis:
            print (li)
        # 输出格式： 第六百二十九章  拍卖结束

        



        pass
