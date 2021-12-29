from typing import List

from billiard.context import Process
from billiard.dummy import Manager

from src.service.board_data_service import get_active_codes
from src.service.crawler.crawler import spiders
from src.service.crawler.crawler.spiders import crawl_spider
from src.service.crawler.custom_crawler import CustomCrawler


def crawling_task(page_num, code):
    spider = get_spider(code)
    crawl_spider.page_num = page_num
    manager = Manager()
    return_dic = manager.dict()
    cc = CustomCrawler()
    proc = Process(
        target=cc.crawling_start,
        args=(
            spider,
            code,
            return_dic,
        )
    )
    try_time = 0
    is_success = False
    while try_time < 2 and not is_success:
        try:
            proc.start()
            proc.join()
            is_success = True
        except Exception as e:
            try_time += 1
    if try_time == 2:
        raise Exception(f"사이트에 연결하지 못했습니다. {spider.__name__}")
    return dict(return_dic)


def get_spider(code) -> object:
    return eval(f"spiders.{code.capitalize()}Spider")


def get_all_spider() -> List[object]:
    return [eval(f"spiders.{code.capitalize()}Spider") for code in get_active_codes()]
