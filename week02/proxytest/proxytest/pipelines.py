# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from .db.mysql import ConnDB

class ProxytestPipeline:
    def process_item(self, item, spider):
        print('pipeline....{}'.format(item['ip']))
        dataInfo = {
            'host': '192.168.47.161',
            'port': 3306,
            'user': 'root',
            'password': '1234',
            'db': 'test'
        }

        sqls = ['insert into proxy.ip (ip) values ({});'.format('\"' + item['ip'] +'\"')]

        conn = ConnDB(dataInfo,sqls)
        conn.run()
        print('pipeline....{}'.format(item['ip']))
        return item
