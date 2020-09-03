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

        self.ws.append(['日期','产品名称','评论次数','评论url','产品id','评价','评价count'])

    def process_item(self, item, spider):
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        product_id = hashlib.md5()
        product_id.update(item['product_name'].encode('utf-8'))

        self.ws.append([now_time,
                        item['product_name'],
                        item['product_comment_count'],
                        item['product_comment_url'],
                        product_id.hexdigest()[0:10],
                       str(item['product_comment_content']),
                       len(item['product_comment_content']),]
                       )
        return item

    def close_spider(self,spider):

        self.wb.save(filename=self.file_name)
        self.wb.close()

class ZdmSQLPipline:
    pass

class ConnDB():

    def __init__(self):
        now_day = time.strftime("%Y_%m_%d", time.localtime())
        self.host = '192.168.47.100'
        self.port = 3306
        self.user = 'root'
        self.password = '1234'
        self.db = 'week10'
        self.table_name = 'comment_' + now_day
        self.test_conn()

    def test_conn(self):

        conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.db)
        # 游标建立的时候就开启了一个隐形的事务
        cur = conn.cursor()

        result = []
        sqls = ['CREATE TABLE IF NOT EXISTS ' + self.table_name + ' (id INT UNSIGNED AUTO_INCREMENT, datetime timestamp not null default current_timestamp,product_name VARCHAR(200) NOT NULL,comment_count VARCHAR(10) NOT NULL,product_id VARCHAR(11) NOT NULL,comment_text TEXT ,PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;']
        # sqls = ["show databasesss;"]
        try:
            for command in sqls:
                print(command)
                cur.execute(command)

                # result.append(cur.fetchone())  # 将游标执行的结果列表的第一个元素存储到列表中
                result.append(cur.fetchall())  # 将游标执行的所有结果存储到列表中
            # 关闭游标
            cur.close()
            conn.commit()  # 输入事务执行成功，直接提交
        except:
            conn.rollback()
        conn.close()
        print(result)
    def process_item(self, item, spider):
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.db)

        product_id = hashlib.md5()
        product_id.update(item['product_name'].encode('utf-8'))
        # 游标建立的时候就开启了一个隐形的事务
        cur = conn.cursor()
        result = []
        values = ''' "{}","{}","{}","{}" '''.format(item['product_name'],item['product_comment_count'],product_id.hexdigest()[0:10],item['product_comment_content'])
        sqls = ['insert into '+ self.table_name + ' ( product_name, comment_count,product_id,comment_text ) VALUES (' + values +');']
        try:
            for command in sqls:
                print(command)
                cur.execute(command)
                # result.append(cur.fetchone())  # 将游标执行的结果列表的第一个元素存储到列表中
                result.append(cur.fetchall())  # 将游标执行的所有结果存储到列表中

            # 关闭游标
            cur.close()
            conn.commit()  # 输入事务执行成功，直接提交
        except:
            conn.rollback()
        conn.close()
        print(result)