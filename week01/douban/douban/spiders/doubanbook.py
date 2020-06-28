import scrapy
from scrapy.selector import Selector
from pandas import DataFrame,Series
from ..items import DoubanItem


class DoubanbookSpider(scrapy.Spider):
    name = 'doubanbook'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/top250']

    def parse(self, response):

        # for num in range(1,11):
        bookNameList = []
        bookPriceList = []
        bookPublisherList = []
        for book in Selector(response=response).xpath('//tr[@class="item"]'):
            bookname = book.xpath('./td[2]/div/a/@title').extract()
            bookinfo = book.xpath('./td[2]/p[@class="pl"]/text()').extract()
            bookpricelist = bookinfo[0].split("/")
            item = DoubanItem()
            item['bookname'] = bookname[0]
            item['bookpublisher'] = bookpricelist[-3]
            item['bookprice'] = bookpricelist[-1]

            yield item
            # bookNameList.append(bookname[0])
            # bookPriceList.append(bookpricelist[-1])
            # bookPublisherList.append(bookpricelist[-3])
            # print(bookname,bookprice,bookpublisher)

        # data = {
        #     "书名": Series(data=bookNameList),
        #     "出版社": Series(data=bookPublisherList),
        #     "价格": Series(data=bookPriceList)
        # }
        #
        # df = DataFrame(data)
        # df.to_csv(path_or_buf='./book.csv', index=False, encoding='utf_8_sig')