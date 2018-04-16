# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from dongguan.items import DongguanItem
import json
class DongguanPipeline(object):
    # def process_item(self, item, spider):
    #     return item
    def open_spider(self,spider):
        # self.start_time = time.time()
        #在spider开始时创建数据库链接，
        try:
            self.con = pymysql.connect(host="123.206.60.72", port=13306, user="root", passwd="123456",db='Myhome',use_unicode = True,charset='utf8')
        #使用cursor()方法获取操作游标
            self.cursor = self.con.cursor()
            print('数据库连接成功')
        except Exception as e:
            print(e)
    def process_item(self, item, spider):
        if isinstance(item,DongguanItem):
            try:
                insert_sql = '''INSERT INTO dongguan(ID, TITLE, ADDRESS, HANDLING, DATIME) VALUES ('{}', '{}', '{}', '{}', '{}')'''.format(item['Id'],item['title'],item['address'],item['handling'],item['datime'])
        # 使用游标执行sql语句
                self.cursor.execute(insert_sql)
        # 提交到数据库执行
                self.con.commit()
                print('数据插入成功')
            except Exception as e:
                print(e)
        return item


    def close_spider(self, spider):
        #spider关闭之前关闭数据库链接
        self.con.close()
        #print(time.time()-self.start_time)

class DongguanjsonPipeline(object):
    def open_spider(self,spider):
        self.filename = open("dongguan.json","w")
    def process_item(self, item, spider):
        content = json.dumps(dict(item),ensure_ascii=False) + ",\n"
        self.filename.write(content)
        return item
    def close_spider(self,spider):
        self.filename.close()





























