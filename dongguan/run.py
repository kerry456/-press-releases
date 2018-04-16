'''
auth:hexl
'''
from dongguan.spiders.dong import DongSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# 获取settings.py模块的设置
settings = get_project_settings()
process = CrawlerProcess(settings=settings)

#添加spider
process.crawl(DongSpider)
#启动spider
process.start()