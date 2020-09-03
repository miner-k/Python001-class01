import scrapy
from scrapy.selector import Selector

class ZdmcommentSpider(scrapy.Spider):
    name = 'zdmcomment'
    allowed_domains = ['smzdm.com']
    # start_urls = ['https://www.smzdm.com/p/24395537/#comments']  # 3页
    # start_urls = ['https://www.smzdm.com/p/24440090/#comments']  # 0页
    start_urls = ['https://www.smzdm.com/p/24439463/#comments']  # 17页



    def parse(self, response):
        list = []
        for item in Selector(response=response).xpath('//*[@class="comment_list"]'):

            for i in item.xpath('.//*[@itemprop="description"]/text()').extract():
                list.append(i)
        print(list)

        if len(Selector(response=response).xpath('//*[@class="pagination"]')) == 0 :
            pass
        else:

            comment_page = Selector(response=response).xpath('//*[@class="pagination"]')[0]
            page_count = comment_page.xpath('./li')[-4].xpath('./a/text()').extract()[0]
            print(page_count)
            comment_url_list = []

            for num in range(2,int(page_count)+1):
                comment_url_head = self.start_urls[0].split('#comments')[0]

                comment_url_list.append(comment_url_head + 'p' + str(num) + '#comments')

            # print(len(comment_page.xpath('./li')))

            print(comment_url_list)

        # for num in range(2, len(comment_page.xpath('./li')) + 1):
        #     url = './li[' + str(num) + ']/a/@href'
        #     # print(url)
        #     print("%" * 20)
        #     print(comment_page.xpath('./li[' + str(num) + ']/@class'))
        #
        #     if comment_page.xpath('./li[' + str(num) + ']/@class') == 'pagedown':
        #         print("下一页")
        #         break
        #     print(url)
        #     url = comment_page.xpath(url).extract()
        #     print(url)
            # yield scrapy.Request(url=url[0],callback=self.get_comment,encoding='utf-8')



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
