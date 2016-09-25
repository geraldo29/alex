
from scrapy.spiders import CrawlSpider, Rule, BaseSpider, Spider
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from courses.items import Course


class Alex(CrawlSpider):
    name = 'uprm.edu'
    allowed_domains = ['uprm.edu']
    start_urls = ['http://www.uprm.edu/cms/index.php?a=file&fid=11777']

    rules = (
        Rule(LxmlLinkExtractor(
             allow=('.*/home.uprm.edu/horario.php#', ),
        ), callback='parse_item'),

        Rule(LxmlLinkExtractor(
            allow=('.*/cms/.*',),
        )),
    )

    def parse_item(self, response):
        
            item = Course()
            item['site'] = 'uprm.edu'
            item["institute"] = "University of Puerto Rico at Mayaguez"
            item['title'] = response.xpath('//li/text()').extract()[0]
            item['id'] = response.xpath('//li/text()').extract()[0]
            item['credits'] = response.xpath('//li/text()').extract()[0][0]
            item['description'] = response.xpath('//li/text()').extract()[0]
            item['category'] = response.xpath('//li/text()').extract()[0]
            yield item
