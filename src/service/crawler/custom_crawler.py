import os
from typing import Dict, List

from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from config.develop_config import SCRAPY_SETTINGS_MODULE


def get_scrapy_settings():
    scrapy_settings = Settings()
    os.environ['SCRAPY_SETTINGS_MODULE'] = SCRAPY_SETTINGS_MODULE
    settings_module_path = os.environ['SCRAPY_SETTINGS_MODULE']
    scrapy_settings.setmodule(settings_module_path, priority='project')
    return scrapy_settings


class CustomCrawler:

    def __init__(self):
        self.output = None

    def _yield_output(self, data):
        self.output = data

    def crawling_start(
            self,
            spider: object,
            code: str,
            return_dic: Dict) -> Dict:
        process = CrawlerProcess(get_scrapy_settings())
        crawler = process.create_crawler(spider)
        process.crawl(crawler, args={'callback': self._yield_output})
        process.start()
        return_dic[code] = self.output

        # stats = crawler.stats   # <class 'scrapy.statscollectors.MemoryStatsCollector'>
        stats = crawler.stats.get_stats()   # <class 'dict'>
        return stats
