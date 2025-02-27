import scrapy
from dpcq.items import ChapterItem
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

class ChaptersSpider(scrapy.Spider):
    name = "chapters"
    allowed_domains = ["www.doupocangqiong.org"]
    start_urls = ["https://www.doupocangqiong.org/doupocangqiong/"]


    def parse(self, response):
        # 提取章节列表的链接和名称
        item = ChapterItem()

        novel_chapters = response.xpath('//div[@class="m-book-list"]/div[@id="play_0"]/ul/li/a/text()').getall()[0:30]
        for novel_chapter in novel_chapters:
            self.logger.info(f"Novel chapter: {novel_chapter}")

        item['chapter'] = novel_chapters
        # print(f"chapter name: {item}")


        novel_chapters_links = response.xpath('//div[@class="m-book-list"]/div[@id="play_0"]/ul/li/a/@href').getall()[0:30]
        # @href：选择 a 标签的 href 属性值，即链接的地址。
        # for novel_chapters_link in novel_chapters_links[0:9]:

        item['link'] = novel_chapters_links
        print(f"chapter item: {item}")

                # yield chapter_item
        if item['chapter']:
            yield item
        else:
            self.logger.error("Chapter is None")


            