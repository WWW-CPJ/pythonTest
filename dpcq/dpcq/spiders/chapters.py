import scrapy
from dpcq.items import ChapterItem


class ChaptersSpider(scrapy.Spider):
    name = "chapters"
    allowed_domains = ["www.doupocangqiong.org"]
    start_urls = ["https://www.doupocangqiong.org/doupocangqiong/"]

    def parse(self, response):
        # 提取章节列表的链接和名称
        item = ChapterItem()

        novel_chapters = response.xpath('//div[@class="m-book-list"]/div[@id="play_0"]/ul/li/a/text()').getall()[0:10]
        for novel_chapter in novel_chapters[0:9]:
            self.logger.info(f"Novel chapter: {novel_chapter}")

        item['name'] = novel_chapters
        # print(f"chapter name: {item}")


        novel_chapters_links = response.xpath('//div[@class="m-book-list"]/div[@id="play_0"]/ul/li/a/@href').getall()[0:10]
        # @href：选择 a 标签的 href 属性值，即链接的地址。
        # for novel_chapters_link in novel_chapters_links[0:9]:

        item['link'] = novel_chapters_links
        print(f"chapter item: {item}")

                # yield chapter_item
        if item['name']:
            yield item
        else:
            self.logger.error("Chapter is None")


            