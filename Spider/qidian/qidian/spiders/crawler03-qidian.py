import scrapy


class QidianSpider(scrapy.Spider):
    name = "qidian"
    allowed_domains = ["qidian.com"]        # 允许爬取的域名,这个参数用于限制爬虫只能抓取指定域名下的网页内容。它可以帮助防止爬虫访问不相关或不允许的域名，确保抓取的范围在预定的域内。
    start_urls = ["https://qidian.com/free/all"]     # 一开始爬取的URL,爬虫会从这个网址出发，开始访问和抓取网页内容。
       # 如果想要抓取多页数据，可这样写
    # start_urls = [
    #     'https://www.qidian.com/rank/hotsales?style=1',
    #     'https://www.qidian.com/rank/hotsales?style=1&page=2',  # page是翻页的参数
    #     'https://www.qidian.com/rank/hotsales?style=1&page=3',
    #     'https://www.qidian.com/rank/hotsales?style=1&page=4',
    #     'https://www.qidian.com/rank/hotsales?style=1&page=5'
    # ]



# 解析函数
    def parse(self, response):    # 该方法用于对response对象进行数据解析
        print(response)           # <200 http://www.4399.com/flash/>
        print(response.text)      # 打印页面源代码
        response.xpath()          # 通过xpath解析数据
        response.css()            # 通过css 解析数据
        # response.xpath() 和 response.css() 是两种解析数据的方式，你可以根据自己的需要选择使用其中一种，也可以同时使用。

        # # 获取免费小说的书名
        # txt = response.xpath('//div[@class="main-content-wrap fl"]/div[@class="all-book-list"]/ul[@class="all-img-list cf"]/li/h2/text()')
        # # txt 列表中的每一项是一个Selector：
        # # <Selector query='//ul[@class="n-game cf"]/li/a/b/text()' data='逃离克莱蒙特城堡'>]
        # # 要通过extract()方法拿到data中的内容
        # print (txt)

        # txt = response.xpath('//div[@class="main-content-wrap fl"]/div[@class="all-book-list"]/ul[@class="all-img-list cf"]/li/h2/text()').extract()
        # print (txt)


        # 也可以先拿到每个li，然后再提取名字
        lis = response.xpath('//ul[@class="all-img-list cf"]/li')
        for li in lis:
            # name = li.xpath('./h2/text()').extract()
            # # name 是一个列表
            # print (name)

            # 一般会这么写，li.xpath('./h2/text()').extract()[0]
            # 但是如果这样列表为空就会报错，所以换另一种写法
            # extract_first 方法取列表中的第一个，如果列表为空，返回NOne
            name = li.xpath('./h2/text()').extract_first()
            print (name)
            # 如果希望得到一个字符串而不是列表，可以使用get方法，
            # name = li.xpath('./h2/text()').get(default='N/A')  # 如果没有找到，返回 'N/A'
            words = li.xpath('./p[@class="update"]/span[@class="HVPGnCzc"]/text()').extract_first()
            chapter = li.xpath('./p[@class="update"]/a/text()').extract_first()
            print (words, chapter)

            # 通过yield 向管道传输数据
            dic = {
                'name': name,
                'words': words,
                'chapter': chapter
            }
            # 可以认为这里是把数据返回给了管道pipline,
            # 但是实际上是先给引擎，然后引擎再给管道，只是这个过程不用我们关心，scrapy会自动完成
            # 这里的数据会在管道程序中接收到
            yield dic







        
