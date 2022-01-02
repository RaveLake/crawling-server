from src.dto.request import NoticeRefreshRequest
from src.mapper import notice_mapper
from src.service import board_data_service
from src.service.crawling_service import crawling_task
from src.service.entity import notice_entity_service, board_data_entity_service


def crawling_notices(request: NoticeRefreshRequest):
    if request.all:
        targets = [board_data.code for board_data in board_data_service.get_active_board_datas()]
    else:
        targets = request.targets
    results = []
    for target in targets:
        results += crawling_task(request.page, target)[target]
    notice_entities = notice_mapper.to_notice_entity(results)
    notice_entity_service.save_notices(notice_entities)
