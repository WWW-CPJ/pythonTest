# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class DpcqPipeline:
    def  __init__(self):
        self.conn = None
        self.cursor = None

    def open_spider(self, spider):
        self.conn = sqlite3.connect('dpcq.db')
        self.cursor = self.conn.cursor()

        # 创建表，如果表不存在的话
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS dpcq (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            author TEXT,
                            info TEXT,
                            intro TEXT,
                            chapter TEXT
                            )
         ''')
        
    def close_spider(self, spider):
        if self.conn:
            self.conn.commit()
            self.conn.close()

    def process_item(self, item, spider):

        try:
            # 确保 item['chapter'] 是一个列表并且每个元素都是字符串
            if isinstance(item['chapter'], list):
                # 如果是列表，确保每个元素都是字符串
                chapters = [str(chapter) for chapter in item['chapter']]
                # 将章节列表转换为逗号分隔的字符串
                chapters_str = ','.join(chapters)
            else:
                # 如果不是列表，直接设置为空字符串
                chapters_str = ''


            self.cursor.execute('''
                                INSERT INTO dpcq (name, author, info, intro, chapter)
                                VALUES (?, ?, ?, ?, ?)''', (item['name'], item['author'], item['info'], item['intro'], chapters_str))
            return item
        except sqlite3.Error as e:
            spider.logger.error(f"Error inserting item into database: {e}")
            return None
