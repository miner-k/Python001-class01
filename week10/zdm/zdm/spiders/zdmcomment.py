import scrapy
from scrapy.selector import Selector

class ZdmcommentSpider(scrapy.Spider):
    name = 'zdmcomment'
    allowed_domains = ['smzdm.com']
    start_urls = ['https://www.smzdm.com/p/24395537/#comments']



    def parse(self, response):

        for item in Selector(response=response).xpath('//*[@class="comment_list"]'):

            print(item.xpath('.//*[@itemprop="description"]/text()').extract())

        print("@" * 10)
        comment_page = Selector(response=response).xpath('//*[@class="pagination"]')[0]
        print("#" * 10)
        for num in range(2, len(comment_page.xpath('./li')) + 1):
            url = './li[' + str(num) + ']/a/@href'
            print(url)
            print("%" * 20)
            print(comment_page.xpath('./li[' + str(num) + ']/@class="pagedown"'))
            if comment_page.xpath('./li[' + str(num) + ']/@class="pagedown"'):
                break
            print(url)
            yield scrapy.Request(url=url,callback=self.get_comment)



    def get_comment(self,response):


        for item in Selector(response=response).xpath('//*[@class="comment_list"]'):

            print(item.xpath('.//*[@itemprop="description"]/text()').extract())


        # for i in response.xpath('//*[@class="comment_list"]'):
        #         # print(i.xpath('./*[@class="z-feed-img"]/a/img/@alt'))
        #         a_html = i.xpath('.//*[@itemprop="description"]/text()')
        # print(response.text)
        # with open('index2.html','w',encoding='utf-8') as file:
        #     print("#" * 1)
        #     file.write(str(response.text))

        pass
