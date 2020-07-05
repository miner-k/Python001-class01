import scrapy
import json
from items import ProxytestItem

class AgentipSpider(scrapy.Spider):
    name = 'agentip'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']

    def parse(self, response):
        # print(response.text)
        ip_json = json.loads(response.text)

        item = ProxytestItem()
        item['ip'] = ip_json['origin']

        yield item