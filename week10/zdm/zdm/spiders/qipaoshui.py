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
                comment_request = scrapy.Request(url=product['product_comment_url'],callback=self.getComment)
                comment_request.meta['product'] = product
                yield comment_request


    def getComment(self,response):

        product = response.meta['product']
        product['product_comment_content'] = []
        for item in Selector(response=response).xpath('//*[@class="comment_list"]'):

            for comment in item.xpath('.//*[@itemprop="description"]/text()').extract():

                if comment.strip(' ') == '':
                    continue
                product['product_comment_content'].append(comment)


        if len(Selector(response=response).xpath('//*[@class="pagination"]')) == 0:
            yield product
        else:

            comment_page = Selector(response=response).xpath('//*[@class="pagination"]')[0]
            page_count = comment_page.xpath('./li')[-4].xpath('./a/text()').extract()[0]
            # print(page_count)
            # comment_url_list = []

            for num in range(2, int(page_count) + 1):
                comment_url_head = product['product_comment_url'].split('#comments')[0]

                # comment_url_list.append(comment_url_head + 'p' + str(num) + '#comments')
                next_page_url = comment_url_head + 'p' + str(num) + '#comments'
                comment_request = scrapy.Request(url=next_page_url, callback=self.get_onepage_comment)
                comment_request.meta['product'] = product
                yield comment_request

            yield product

    def get_onepage_comment(self,response):

        product = response.meta['product']
        product['product_comment_content'] = []
        for item in Selector(response=response).xpath('//*[@class="comment_list"]'):

            for comment in item.xpath('.//*[@itemprop="description"]/text()').extract():

                if comment.strip(' ') == '':
                    continue
                product['product_comment_content'].append(comment)



