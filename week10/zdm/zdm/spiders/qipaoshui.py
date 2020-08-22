import scrapy


class QipaoshuiSpider(scrapy.Spider):
    name = 'qipaoshui'
    allowed_domains = ['smzdm.com']
    start_urls = ['https://www.smzdm.com/fenlei/qipaoshui/']

    def parse(self, response):
        pass
