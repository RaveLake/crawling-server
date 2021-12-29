from typing import *

from src.entity.BoardData import BoardData
from src.service.board_data_service import get_active_board_datas, get_board_data
from src.service.crawler.crawler.spiders.crawl_spider import DefaultSpider

page_num = 1
manual_spiders = {
    'knudorm'
}
board_datas = get_active_board_datas()
# Spider Class 자동 생성
for board_data in board_datas:
    if 'test' not in board_data.code and board_data.code not in manual_spiders:
        txt = f"""
class {board_data.code.capitalize()}Spider(DefaultSpider):
    def __init__(self, **kwargs):
        self.try_time = 0

        self.name = board_data.name
        if board_data.key_name_page:
            url:str = board_data.uri_root
            if board_data.key_name_page == 'restful':
                url_page = url + '/' + '%d'
            elif board_data.key_name_page == 'offset':
                url_page = url
            else:
                url_page = url + '&' + board_data.key_name_page + '=%d'
            if board_data.key_name_page == 'offset':
                urls = [url_page % ((i-1)*20) for i in range(1, page_num+1)]
            else:
                urls = [url_page % i for i in range(1, page_num+1)]
            self.start_urls = urls
        else:
            self.start_urls = [board_data.uri_root]

        self.output_callback = kwargs.get('args').get('callback')
        self.scraped_info_data = []
        super().__init__(**kwargs)
        super().set_args(board_data)
"""
        exec(compile(txt, "<string>", "exec"))
