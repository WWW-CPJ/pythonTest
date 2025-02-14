import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


from itemadapter import ItemAdapter
import sqlite3
from dpcq.items import ChapterItem

from django_setup import setup_django_env
from search_project.search_app.models import SearchItem
setup_django_env()


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
                            chapter TEXT,
                            link TEXT
                )
         ''')
        
    def close_spider(self, spider):
        if self.conn:
            self.conn.commit()
            self.conn.close()

    def process_item(self, item, spider):

        print ("开始处理章节")
        print (f"chapter item: {item}")

        if item is None:
            spider.logger.error("Item is None")
            return None

        try:
            if isinstance(item, ChapterItem):
                for chapter_name, chapter_link in zip(item['chapter'], item['link']):

                    # 使用 Django 模型创建新纪录
                    SearchItem.objects.create(chapter=chapter_name, link=chapter_link)

                    # 使用 SQLite 原生 SQL 语句创建新纪录
                    self.cursor.execute('''
                                    INSERT INTO chapters (chapter, link)
                                    VALUES (?, ?)''', (chapter_name, chapter_link, ))
                inserted_id = self.cursor.lastrowid

                if inserted_id:
                    print(f"Data inserted successfully with ID: {inserted_id}")
                else:
                    print("Data insertion failed.")
                self.conn.commit()

                return item
            else:
                print("Item is not an instance of ChapterItem")
                print(f"chapter_item: {item}")
                print(f"Type of chapter_item: {type(item)}")
                return None
        except sqlite3.Error as e:
            spider.logger.error(f"Error inserting item into database:{e}")
            self.conn.rollback()
            # 撤销当前事务中的所有操作，如果在事务中发生了错误（比如插入数据时遇到了问题），rollback()方法会撤销之前的所有更改。
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