import scrapy
from scrapy.selector import Selector
from ..items import ZdmItem


class QipaoshuiSpider(scrapy.Spider):
    name = 'qipaoshui'
    allowed_domains = ['smzdm.com']
    start_urls = ['https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/#feed-main/']

    def parse(self, response):

        # print(response.text)


        for item in Selector(response=response).xpath('//*[@class="feed-block z-hor-feed"]'):

            product = ZdmItem()
            product['product_name'] = str(item.xpath('./*[@class="z-feed-img"]/a/img/@alt').extract()[0])

            a_html = item.xpath('./div[@class="z-feed-content "]/div["z-feed-foot"]/div[@class="z-feed-foot-l"]')
            for a in a_html:
                product['product_comment_url'] = a.xpath('./a[2]/@href').extract()[0]
                product['product_comment_count'] = a.xpath('./a[2]/@title').extract()[0].split()[-1]

                # print(product_comment_url,product_comment_count,product_name)
                yield product


