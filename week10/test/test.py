

import lxml.etree


with open('index2.html','r',encoding='utf-8') as f:

    # response = lxml.etree.htmlfile(f.read())
    response = lxml.etree.HTML(f.read())

    # print(len(response.xpath('//*[@class="pagination"]/li')))
    # for i in response.xpath('//*[@class="pagination"]'):
        # print(i.xpath('./*[@class="z-feed-img"]/a/img/@alt'))
    i = response.xpath('//*[@class="pagination"]')[0]
    url_list = []
    for num in range(1,len(i.xpath('./li'))+1):
        url = './li[' + str(num) +']/a/@href'

        if i.xpath('./li[' + str(num) +']/@class="pagedown"'):
            break
        url_list.append(i.xpath(url)[0])
    print(url_list)
    # a_html = i.xpath('.//*[@itemprop="description"]/text()')

    '''//*[@class="pagination"]/li[@class="pagedown"]/a/@href'''
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