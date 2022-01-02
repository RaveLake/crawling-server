from typing import List

from src.entity.BoardData import BoardData
from src.service.entity.board_data_entity_service import find_all_by_crawling_status, find_by_code


def get_active_codes() -> List[str]:
    board_datas = find_all_by_crawling_status('00')
    return [board_data.code for board_data in board_datas]


def get_active_board_datas() -> List[BoardData]:
    return find_all_by_crawling_status('00')


def get_board_data(code: str) -> BoardData:
    return find_by_code(code)
