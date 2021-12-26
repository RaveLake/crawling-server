from __future__ import absolute_import, unicode_literals

import os
import sys
from typing import Dict, List

from develop_config import SCRAPY_SETTINGS_MODULE
from src.service import board_data_service
import billiard
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from src.service.crawler.crawler.spiders.crawl_spider import DefaultSpider

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def get_spider(code) -> DefaultSpider:
    return eval(f"crawl_spider.{code.capitalize()}Spider")


def get_all_spider() -> List[DefaultSpider]:
    return [eval(f"crawl_spider.{code.capitalize()}Spider") for code in board_data_service.get_active_codes()]


def get_scrapy_settings():
    scrapy_settings = Settings()
    os.environ['SCRAPY_SETTINGS_MODULE'] = SCRAPY_SETTINGS_MODULE
    settings_module_path = os.environ['SCRAPY_SETTINGS_MODULE']
    scrapy_settings.setmodule(settings_module_path, priority='project')
    return scrapy_settings


class CustomCrawler:

    def __init__(self):
        self.manager = billiard.Manager()
        self.output = None

    def _yield_output(self, data):
        self.output = data

    def crawling_start(
            self,
            scrapy_settings: Settings,
            spider: DefaultSpider,
            code: str,
            ) -> Dict:
        process = CrawlerProcess(scrapy_settings)
        crawler = process.create_crawler(spider)
        process.crawl(crawler, args={'callback': self._yield_output})
        process.start()
        # return_dic[code] = self.output

        # stats = crawler.stats   # <class 'scrapy.statscollectors.MemoryStatsCollector'>
        stats = crawler.stats.get_stats()   # <class 'dict'>
        return stats

    # def crawl(self, code, page_num):
    #     invalid_board_name = True
    #     spider_arg = None
    #     if code:
    #         board = f"{code.capitalize()}Spider"
    #         try:
    #             spider_arg = [get_spider(board), ]
    #             invalid_board_name = False
    #         except:
    #             pass
    #     else:
    #         spider_arg = get_all_spider()
    #
    #     return_dic = self.manager.dict()
    #     if invalid_board_name and code:
    #         message = "Invalid board name. Request with correct board name to initialize Database."
    #         result_code = 1
    #         return_dic["empty"] = ""
    #     else:
    #         scrapy_settings = self.get_scrapy_settings()
    #         crawl_spider.page_num = page_num
    #         proc_list = []
    #         for spider in spider_arg:
    #             self._crawling_start(
    #                 scrapy_settings,
    #                 spider,
    #                 code,
    #                 return_dic,
    #             )
    #
    #         #     proc = billiard.context.Process(
    #         #         target=self._crawling_start,
    #         #         args=(
    #         #             scrapy_settings,
    #         #             spider,
    #         #             code,
    #         #             return_dic,
    #         #         )
    #         #     )
    #         #     proc.start()
    #         #     proc_list.append(proc)
    #         # for proc in proc_list:
    #         #     proc.join()
    #         message = "Success."
    #         result_code = 0
    #     res = dict()
    #     res["result_code"] = result_code
    #     res["message"] = message
    #     res["output"] = json.dumps(dict(return_dic))
    #     return res
