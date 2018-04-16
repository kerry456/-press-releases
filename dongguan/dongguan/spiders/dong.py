# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
# from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dongguan.items import DongguanItem

class DongSpider(CrawlSpider):
    name = 'dong'
    allowed_domains = ['wz.sun0769.com']
    offset = 0
    base_urls = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page=' + str(offset)
    start_urls = [base_urls]
    # rules = (
    #     Rule(LinkExtractor(allow='type=4&page=\d+'),callback='parse_item',follow=False),
    #     # Rule(LinkExtractor(allow=r'/html/question/\d+/\d+.shtml'), callback='parse_item'),
    #     # Rule(LinkExtractor(allow=r'/html/question/\d+/\d+.shtml'), callback='content_item'),
    # )

    def parse(self, response):
        item = DongguanItem()
        node_list = response.xpath('//*[@id="morelist"]/div/table[2]//tr/td/table')
        for node in node_list:
            id_list = node.xpath('.//tr/td[1]/text()').extract()
            title_list = node.xpath('.//tr/td[2]/a[2]/text()').extract()
            address_list = node.xpath('.//tr/td[2]/a[3]/text()').extract()
            handing_list = node.xpath('.//tr/td[3]/span/text()').extract()
            datime_list = node.xpath('.//tr/td[5]/text()').extract()
            # item['content'] = response.xpath('//div[@class="contentext"]/text() | //div[@class="c1 text14_2"]/text()').extract_first()
            for Id,title,address,handling,datime in zip(id_list,title_list,address_list,handing_list,datime_list):
                item['Id'] = Id
                item['title'] = title
                item['address'] = address
                item['handling'] = handling
                item['datime'] = datime
                yield item
            self.offset+=30
            print('正在爬取' + str(self.offset/30) + '页.....')
            if node_list == []:
                return None
            yield scrapy.Request(url='http://wz.sun0769.com/index.php/question/questionType?type=4&page=' + \
                                 str(self.offset),callback=self.parse)
    # def content_item(self,response):
    #     item = DongguanItem()
    #     item['content'] = response.xpath('//div[@class="contentext"]/text() | //div[@class="c1 text14_2"]/text()').extract_first()
    #     yield item
