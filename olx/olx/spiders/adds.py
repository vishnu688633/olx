import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Adds(CrawlSpider):
    name = 'add'
    allowed_domains = ['olx.in']
    #start_urls = ['https://www.olx.in/']

    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(url='https://www.olx.in/', headers={
            'Uger-Agent': self.user_agent
        })

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h3/a"),
             callback='parse_item', follow=True, process_request='set_user_agent'),

        Rule(LinkExtractor(
            restrict_xpaths="//li[@class='next']/a"), process_request='set_user_agent')
    )

    def set_user_agent(self, request):
        request.headers['User-Agent'] = self.user_agent

        return request

    def parse_item(self, response):
        yield {
            'url': response.url,
            'property_name': response.xpath(".//span[@class='_2tW1I']/text()").get()
                  'price':response.xpath(".//span[@class='_89yzn']/text()").get()
            'description':response.xpath(".//span[@class='_25oXN']/text()").get()
            'location':response.xpath(".//span[@class='_1KOFM']/text()").get()
          'property_type': response.xpath(".//span[@class='_2vNpt']/text()").get()
              'bathrooms': response.xpath(".//span[@class='_3_knn']/text()").get()



            # 'User-Agent': response.request.headers['User-Agent']
        }