# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import pymysql

class WangyiyunPipeline:
    collection = "wangyiyun"

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"),
            mongo_db=crawler.settings.get("MONGO_DB")
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = {
            'ID': item["id"],
            '热评': item["content"],
        }
        table = self.db[self.collection]
        table.insert_one(data)
        return item
    # def __init__(self):
    #     # 连接MySQL数据库
    #     self.connect = pymysql.connect(host='localhost', user='root', password='12345678', db='python')
    #     self.cursor = self.connect.cursor()
    #
    # def process_item(self, item, spider):
    #     sql = '''INSERT INTO wangyiyun (id,content) VALUES (%s, %s)'''
    #     self.cursor.execute(sql, (item.get('id'),
    #                               item.get('content'),
    #                               ))
    #     self.connect.commit()
    #     return item
    # def close_spider(self, spider):
    #     self.cursor.close()
    #     self.connect.close()
