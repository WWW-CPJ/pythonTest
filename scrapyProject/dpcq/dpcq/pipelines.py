# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

from dpcq.items import ChapterItem, DpcqItem


class DpcqPipeline:
    def  __init__(self):
        self.conn = None
        self.cursor = None

    def open_spider(self, spider):
        self.conn = sqlite3.connect('dpcq.db')
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
            DROP TABLE IF EXISTS dpcq 
         ''')
        # 创建表，如果表不存在的话
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS dpcq (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            author TEXT,
                            status TEXT,
                            date TEXT,
                            intro TEXT
                            )
         ''')
        
    def close_spider(self, spider):
        if self.conn:
            self.conn.commit()
            self.conn.close()

    def process_item(self, item, spider):
        if isinstance(item, DpcqItem):
            try:
                # 确保字段不为 None，如果为 None，使用空字符串替代            # name = item.get('name', '')          # name = item['name'][0]
                name = item.get('name', '小说')[0]
                author = item.get('author', '作者')[0]
                status = item.get('status', '状态')   # spider 中已经处理了，这里不需要再处理。不需要再提取第一个元素
                date = item.get('date', '日期')
                intro = item.get('intro', '简介')[0]

                self.cursor.execute('''
                                    INSERT INTO dpcq (name, author, intro, status, date)
                                    VALUES (?, ?, ?, ?, ?)''', (name, author, intro, status, date))
                
                # 获取插入数据的主键ID
                inserted_id = self.cursor.lastrowid

                if inserted_id:
                    print(f"Data inserted successfully with ID: {inserted_id}")
                else:
                    print("Data insertion failed.")
                self.conn.commit()

                return item
            except sqlite3.Error as e:
                spider.logger.error(f"Error inserting item into database: {e}")
                return None


class ChaptersPipeline:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def open_spider(self, spider):
        self.conn = sqlite3.connect('chapters.db')
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
            DROP TABLE IF EXISTS chapters
         ''')
        # 创建表，如果表不存在的话
        # SQLite的 TEXT 类型是不限制长度的，可以存储任意长度的字符串，但是如果字符串长度超过1000，会变成BLOB类型，所以这里设置为TEXT类型
        # 包括字母数据，标点符号，特殊字符，空格等等
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS chapters (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            chapter TEXT
                )
         ''')
        
    def close_spider(self, spider):
        if self.conn:
            self.conn.commit()
            self.conn.close()

    def process_item(self, chapter_item, spider):

        # adapter = ItemAdapter(item)
        # chapters = adapter.get('chapter', [])
        # print(f"Chpters from ItemAdapter: {chapters}")

        print ("开始处理章节")
        print (f"chapter_item: {chapter_item}")

        if chapter_item is None:
            spider.logger.error("Item is None")
            return None
        try:
            if isinstance(chapter_item, ChapterItem):
                self.cursor.execute('''
                                    INSERT INTO chapters (chapter)
                                    VALUES (?)''', (chapter_item, ))
                inserted_id = self.cursor.lastrowid

                if inserted_id:
                    print(f"Data inserted successfully with ID: {inserted_id}")
                else:
                    print("Data insertion failed.")
                self.conn.commit()

                return chapter_item
            else:
                print("Item is not an instance of ChapterItem")
                print(f"chapter_item: {chapter_item}")
                print(f"Type of chapter_item: {type(chapter_item)}")
                return None
        except sqlite3.Error as e:
            spider.logger.error(f"Error inserting item into database:{e}")
            self.conn.rollback()
            return None
    
        # if isinstance(chapter_item, ChapterItem):
        #     print ("分割线")
        #     try:
        #         for chapter in chapter_item['chapter']:
        #             self.cursor.execute('''
        #                                 INSERT INTO chapters (chapter)
        #                                 VALUES (?)''', (chapter, ))
        #             inserted_id = self.cursor.lastrowid

        #             if inserted_id:
        #                 print(f"Data inserted successfully with ID: {inserted_id}")
        #             else:
        #                 print("Data insertion failed.")
        #         self.conn.commit()

        #         return chapter_item
        #     except sqlite3.Error as e:
        #         spider.logger.error(f"Error inserting item into database: {e}")
        #         self.conn.rollback()
        #         return None
        # else:
        #     print("Item is not an instance of ChapterItem")
        #     print(f"chapter_item: {chapter_item}")