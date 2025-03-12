import scrapy


class DoupoSpider(scrapy.Spider):
    name = "doupo"
    allowed_domains = ["doupocangqiong.org"]
    start_urls = ["https://www.doupocangqiong.org/doupocangqiong/"]

    def parse(self, response):

        status_code = response.status
        print (status_code)

        lis = response.xpath('//*[@id="play_0"]/ul/li')

        # 第一种
        # # 控制输出前 100 个 <li> 元素
        # for index, li in enumerate(lis):
        #     # 如果已经输出了100个，停止
        #     if index >= 100:
        #         break
            
        #     # 获取 <li> 中的 <a> 标签的文本
        #     text = li.xpath('.//a/text()').get()
            
        #     if text:
        #         print(text)  # 打印 <a> 标签中的文本
        # 第八十六章 挑战

        # 第二种
        # for li in lis:
        #     li = response.xpath('.//li/a/text()').get()
        #     if li:
        #         print(lis[100])
        #     else:
        #         print ("it has error")
        # # 输出格式：  <Selector query='.//li/a/text()' data='第一千六百二十章  斗帝强者的力量！'>,


        # 第三种
        lis = response.xpath('//*[@id="play_0"]/ul/li/a/text()').getall()
        for li in lis:
            print (li)
        # 输出格式： 第六百二十九章  拍卖结束

        



        
