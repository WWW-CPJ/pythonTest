import scrapy
import requests
from bs4 import BeautifulSoup

class DataanalysisSpider(scrapy.Spider):
    name = "dataanalysis"
    allowed_domains = ["woshipm.com"]
    start_urls = ["https://www.woshipm.com/category/data-analysis"]


    def parse(self, response):
        print (f'Status Code: {response.status}')

        url = 'https://www.woshipm.com/data-analysis/6130588.html'
        headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
        response = requests.get(url, headers)

        print (response.status_code)
        # print (response.text)
        # 可以返回网页代码，但是怎么提取想要的字段

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # request.text 是获取到的网页文本，html.parse 是用HTML解析器来解析网页。soup 是一个bs对象

            title = soup.title.string     #提取网页的标题。soup.title 获取 <title> 标签，.string 返回标签内的文本内容（即网页的标题）。
            print ('页面标题：', title)

            paragraphs = soup.find_all('p')  #查找网页中所有的 <p>（段落）标签，并将它们存储在 paragraphs 列表中。find_all 方法会返回匹配的所有标签的列表。
            for p in paragraphs:
                print (p.get_text())

            links = soup.find_all('a')
            for link in links:
                print ('链接文本：', link.get_text(), '| 链接地址：', link['href'])
        else:
            print ("请求失败，状态码为：", response.status_code)


        # # fetch 里的 连接
        # api_url = "https://www.woshipm.com/__api/v3/qrcode_list"
        # api_response = requests.get(api_url)

        # if api_response.status_code == 200:
        #     data = api_response.json()
        #     print (data)
        # else:
        #     print (f'Failed to get {api_url}')


        # # 列表页
        # title = response.xpath('//*[@id="app"]/div/div/div/div[1]/div[2]/article[1]/div[2]/h2/a/text()').get()
        # content = response.xpath('//*[@id="app"]/div/div/div/div[1]/div[2]/article[1]/div[2]/div[1]/text()').getall()
        # author = response.xpath('//*[@id="app"]/div/div/div/div[1]/div[2]/article[1]/div[2]/div[2]/text()').get()

        # print (f'Title: {title}')
        # print (f'Content: {content}')
        # print (f'Author: {author}')

        # dic = {'title': title,
        #        'content': content,
        #        'author': author}
        # yield dic

        # # 文章页
        # title = response.xpath('//*[@id="app"]/div/div/div[2]/div/div[1]/h2/text()').get()
        # author = response.xpath('//*[@id="app"]/div/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/a/text()').get()
        # time = response.xpath('//*[@id="app"]/div/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/time/text()').get()
        # introduce = response.xpath('//*[@id="app"]/div/div/div[2]/div/div[1]/div[3]/blockquote/p/text()').getall()

        # if title:
        #     print (f'title is : {title}')
        # else:
        #     print ("title was not found")
        # print (author)
        # print (time)
        # print (introduce)
        # # 返回值是None
        
