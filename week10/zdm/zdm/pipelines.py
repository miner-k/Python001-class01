# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from openpyxl import Workbook
import  time
import  os
import hashlib

import pymysql
class ZdmPipeline:

    def __init__(self):
        now_day = time.strftime("%Y-%m-%d", time.localtime())
        self.file_name = now_day + '.xlsx'
        if os.path.exists(self.file_name):
            os.remove(self.file_name)
        self.wb = Workbook()
        self.ws = self.wb.active

        self.ws.append(['日期','产品名称','评论次数','评论url','产品id'])

    def process_item(self, item, spider):
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        product_id = hashlib.md5()
        product_id.update(item['product_name'].encode('utf-8'))

        self.ws.append([now_time,item['product_name'],item['product_comment_count'],item['product_comment_url'],product_id.hexdigest()[0:10]])
        return item

    def close_spider(self,spider):

        self.wb.save(filename=self.file_name)
        self.wb.close()

class ZdmSQLPipline:
    pass