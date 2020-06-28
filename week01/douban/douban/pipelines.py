# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from pandas import Series,DataFrame
class DoubanPipeline:
    # bookNameList = bookPriceList = bookPublisherList = []

    def __init__(self):
        self.bookNameList = []
        self.bookPriceList = []
        self.bookPublisherList = []

    def process_item(self, item, spider):

        print(item['bookname'])
        self.bookNameList.append(item['bookname'])
        self.bookPriceList.append(item['bookpublisher'])
        self.bookPublisherList.append(item['bookprice'])

        print(self.bookNameList)
        return item

    def close_spider(self,spider):
        data = {
            "书名": Series(data=self.bookNameList),
            "出版社": Series(data=self.bookPublisherList),
            "价格": Series(data=self.bookPriceList)
        }

        df = DataFrame(data)
        df.to_csv(path_or_buf='./book.csv', index=False, encoding='utf_8_sig',mode='a+')

