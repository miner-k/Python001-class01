

import lxml.etree


# with open('index2.html','r',encoding='utf-8') as f:
#
#     # response = lxml.etree.htmlfile(f.read())
#     response = lxml.etree.HTML(f.read())
#
#     # print(len(response.xpath('//*[@class="pagination"]/li')))
#     # for i in response.xpath('//*[@class="pagination"]'):
#         # print(i.xpath('./*[@class="z-feed-img"]/a/img/@alt'))
#     i = response.xpath('//*[@class="pagination"]')[0]
#     url_list = []
#     for num in range(2,len(i.xpath('./li'))+1):
#         url = './li[' + str(num) +']/a/@href'
#
#         print(i.xpath('./li[' + str(num) +']/@class="pagedown"'))
#         if i.xpath('./li[' + str(num) +']/@class="pagedown"'):
#             break
#         url_list.append(i.xpath(url)[0])
#     print(url_list)
#     # a_html = i.xpath('.//*[@itemprop="description"]/text()')

    # '''//*[@class="pagination"]/li[@class="pagedown"]/a/@href'''
    # for a in a_html:
    #     comment_url = a.xpath('./a[2]/@href')
    #     comment_count = a.xpath('./a[2]/@title')
    #
    #     print(comment_url,comment_count)
    # print(a_html)
    # feed-block z-hor-feed
    # for i in  response.xpath('//*[@class="z-feed-foot-l"]'):
    #     url = i.xpath('./a[2]/@href')[0]
    #     name = i.xpath('./a[2]/@onclick')
    #     # name = name[0].split("pagetitle':'")[-1].split("'")[0]
    #     # ''.strip()
    #     print(url,name)

# print('abc d'.strip('d'))


# import time
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
#
# with open('index1.html', 'w', encoding='utf-8') as file:
#     print("#" * 1)
#     file.write("")


import os
import hashlib
# # a = os.system('md5sum' + 'aaa')
# # print(a)
# a = r'aaa'
# tmp = hashlib.md5().update(a.encode('utf-8'))
# # tmp.update(a.encode('utf-8'))
# # print(tmp.hexdigest()[0:10])
#
# print(tmp.)

# print(' dbncd   '.strip(' '))
import pymysql
import  time
# class ConnDB():
#
#     def __init__(self):
#         now_day = time.strftime("%Y_%m_%d", time.localtime())
#         self.host = '192.168.47.100'
#         self.port = 3306
#         self.user = 'root'
#         self.password = '1234'
#         self.db = 'week10'
#         self.table_name = 'comment_' + now_day
#         self.test_conn()
#
#     def test_conn(self):
#
#         conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.db)
#         # 游标建立的时候就开启了一个隐形的事务
#         cur = conn.cursor()
#
#         result = []
#         sqls = ['CREATE TABLE IF NOT EXISTS ' + self.table_name + ' (id INT UNSIGNED AUTO_INCREMENT,product_name VARCHAR(200) NOT NULL,comment_count VARCHAR(10) NOT NULL,product_id VARCHAR(11) NOT NULL,comment_text TEXT ,PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;']
#         # sqls = ["show databasesss;"]
#         try:
#             for command in sqls:
#                 print(command)
#                 cur.execute(command)
#
#                 # result.append(cur.fetchone())  # 将游标执行的结果列表的第一个元素存储到列表中
#                 result.append(cur.fetchall())  # 将游标执行的所有结果存储到列表中
#             # 关闭游标
#             cur.close()
#             conn.commit()  # 输入事务执行成功，直接提交
#         except:
#             conn.rollback()
#         conn.close()
#         print(result)
#     def run(self):
#         conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.db)
#
#         # 游标建立的时候就开启了一个隐形的事务
#         cur = conn.cursor()
#         result = []
#         sqls = ['insert into '+ self.table_name + ' ( product_name, comment_count,product_id,comment_text ) VALUES (' + '"name",6,"12scdde","cdddd"' +');']
#         try:
#             for command in sqls:
#                 print(command)
#                 cur.execute(command)
#                 result.append(cur.fetchone())  # 将游标执行的结果列表的第一个元素存储到列表中
#                 result.append(cur.fetchall())  # 将游标执行的所有结果存储到列表中
#
#             # 关闭游标
#             cur.close()
#             conn.commit()  # 输入事务执行成功，直接提交
#         except:
#             conn.rollback()
#         conn.close()
#         print(result)
# conn = ConnDB()
# conn.run()

# import pandas as pd
# s1 = pd.Series(data=[1,2,3,None,3,4])
# pd1 = pd.DataFrame(data={'product':s1})
# # pd1.append(s1,ignore_index=True)
# pd1['name'] = "aaa"
# print(pd1)
# pd1.drop_duplicates(inplace=True)
# pd1.dropna(inplace=True)
# print(pd1)

# from snownlp import SnowNLP
#
# text = "每卖一部手机，芯片就少一块，你不买我不买，它还能撑3年"
# s = SnowNLP(text)
# a = s.sentiments
# print("#" * 20)
# print(s.sentiments)
#
# if __name__ == '__main__':
#     print("#")
#
# print('cdsshuaweilcld'.find('huawei'))
#
# # for k,v in {'a':1,'b':2}.items():
# #     print(k,v)
#
#
# a = {'a':1,'b':2}
# a.pop('a')
# print(list(a.keys()))
# 3.12222
import os
# print(round(7/3 *100))
# print()

import importlib





import importlib

moudels_dir = 'model1'
params = importlib.import_module(moudels_dir) #绝对导入
print(dir(params))
