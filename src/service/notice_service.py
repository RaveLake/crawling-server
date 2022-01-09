from src.dto.request import NoticeRefreshRequest
from src.mapper import notice_mapper
from src.service.board_data_service import get_active_board_datas
from src.service.crawling_service import crawling_task
from src.service.entity import notice_entity_service


def crawling_notices(session, request: NoticeRefreshRequest):
    if request.all:
        targets = [board_data.code for board_data in get_active_board_datas(session)]
    else:
        targets = request.targets
    results = []
    for target in targets:
        d = crawling_task(request.page, target)
        print(d)
        results += d[target]
    notice_entities = notice_mapper.to_notice_entity(results)
    notice_entity_service.save_notices(session, notice_entities)
