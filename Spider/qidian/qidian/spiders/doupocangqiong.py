import scrapy


class DoupocangqiongSpider(scrapy.Spider):
    name = "doupocangqiong"
    allowed_domains = ["doupoucangqiong.org"]
    start_urls = [f"https://www.doupocangqiong.org/doupocangqiong/{i}].html" for i in range (18096, 24639394)]

    def parse(self, response):

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
        }
        for url in self.start_urls:
            yield scrapy.Request (headers=headers, url=url, callback=self.parse)

        chapter_name = response.xpath('/html/body/div[2]/div/div[2]/h1/text()').get()
        print (chapter_name)

        content = response.xpath('//*[@id="content"]/text()').getall()
        print (content)
        # ['\r\n', '\r\n', '\r\n\r\n\xa0\xa0\xa0\xa0', '\xa0\xa0\xa0\xa0“斗之力，三段！”', '\xa0\xa0\xa0\xa0望   
        # 结果中含有换行符等

        # 确定下一页的url
        current_id = int (response.url.split('/')[-1].split('.')[0])
        # 获取当前页面的ID
        next_id = current_id +1    # 生成下一个页面的ID
        next_url = f"https://www.doupocangqiong.org/doupocangqiong/{next_id}.html"

        # 如果下一个页面仍在范围内，则继续爬取
        if next_id <= 18099:             #根据需要设定上限
            yield scrapy.Request (url=next_url, headers=headers, callback=self.parse)






        pass
