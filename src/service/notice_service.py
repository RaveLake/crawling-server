import logging

from src.config.database import session_scope
from src.dto.request import NoticeRefreshRequest
from src.mapper import notice_mapper
from src.service.board_data_service import get_active_board_datas
from src.service.crawling_service import crawling_task
from src.service.entity import notice_entity_service

logger = logging.getLogger()


def crawling_notices(request: NoticeRefreshRequest):
    logger.debug("crawling_notices start")
    if request.all:
        with session_scope() as session:
            targets = [board_data.code for board_data in get_active_board_datas(session)]
    else:
        targets = request.targets
    logger.debug(f"targets: {targets}")
    results = []
    for target in targets:
        d = crawling_task(request.page, target)
        logger.debug(f"crawling_task end - {target}:{request.page}")
        results += d[target]
    notice_entities = notice_mapper.to_notice_entity(results)
    with session_scope() as session:
        notice_entity_service.save_notices(session, notice_entities)
