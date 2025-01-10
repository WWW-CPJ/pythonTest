import scrapy
import requests
from dpcq.items import DpcqItem, ChapterItem
import xml.etree.ElementTree as ET

class DocqhomeSpider(scrapy.Spider):
    name = "dpcqHome"
    allowed_domains = ["www.doupocangqiong.org"]
    start_urls = ["https://www.doupocangqiong.org/doupocangqiong/"]

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Referer': 'https://www.doupocangqiong.org/',
    'Origin': 'https://www.doupocangqiong.org',
    'Priority': 'u=1, i',
    'Sec-Ch-Ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site'
    }
        
    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield scrapy.Request(url, headers=self.headers, callback=self.parse)

    def parse(self, response):

        status_code = response.status
        self.logger.info(f'Status Code: {status_code}')

        item = DpcqItem()
        book_info = response.xpath('//div[@class="m-book_info"]/div[@class="m-infos"]')
        book_info_text = response.xpath('//div[@class="m-book_info"]/div[@class="m-infos"]//text()').getall()
        # item['info'] = book_info_text
        item ['status'] = book_info_text[2]
        item['date'] = book_info_text[3]
        self.logger.info(f"Book info: {book_info_text}")

        novel_name = book_info.xpath('//h1/text()').getall()
        item['name'] = novel_name
        self.logger.info(f'Novel Name: {novel_name}')
        novel_author = book_info.xpath('//div[@class="m-book_info"]/div[@class="m-infos"]/span[1]/text()').getall()
        item['author'] = novel_author
        self.logger.info(f"Novel Author : {novel_author}")

        novel_introduce = book_info.xpath('//div[@class="m-book_info"]/p/text()').getall()
        item['intro'] = novel_introduce
        self.logger.info(f"Novel Introduce: {novel_introduce}")
               
        yield item

        chapter_item = ChapterItem()
        novel_chapters = response.xpath('//div[@class="m-book-list"]/div[@id="play_0"]/ul/li/a/text()').getall()[0:10]
        for novrl_chapter in novel_chapters[0:2]:
            self.logger.info(f"Novel chapter: {novrl_chapter}")
        chapter_item['chapter'] = novel_chapters[0:2]
        # print (novel_chapters[0:2])
        print(f"item: {chapter_item}")
        # yield chapter_item
        if chapter_item['chapter']:
            yield chapter_item
        else:
            self.logger.error("Chapter is None")

 



        # yield self.create_xml(item).
        
    # def create_xml(self, item):
    #     # 创建根节点
    #     root = ET.Element('item')
        
    #     # 创建 'info' 节点
    #     info = ET.SubElement(root, 'info')
    #     ET.SubElement(info, 'value').text = '斗破苍穹'
    #     ET.SubElement(info, 'value').text = '作者：天蚕土豆'
    #     ET.SubElement(info, 'value').text = '状态： 连载中'
    #     ET.SubElement(info, 'value').text = '日期：2021-06-05 09:59:44'
        
    #     # 添加书名
    #     ET.SubElement(root, 'name').text = item.get('name', '未知')
        
    #     # 添加作者
    #     ET.SubElement(root, 'author').text = item.get('author', '未知')
        
    #     # 添加简介
    #     ET.SubElement(root, 'intro').text = item.get('intro', '无简介')
        
    #     # 添加章节
    #     chapter = ET.SubElement(root, 'chapter')
    #     for ch in item.get('chapter', []):
    #         ET.SubElement(chapter, 'value').text = ch
        
    #     # 格式化 XML 输出并返回
    #     tree = ET.ElementTree(root)
        
    #     # 使用 minidom 格式化输出（添加缩进和换行）
    #     import xml.dom.minidom
    #     xml_str = xml.dom.minidom.parseString(ET.tostring(root)).toprettyxml(indent="  ")

    #     # 返回格式化后的 XML 字符串
    #     return xml_str