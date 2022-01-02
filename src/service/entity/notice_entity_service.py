import logging
from collections import defaultdict
from typing import List

from config.database import session
from src.entity.Notice import Notice
from src.util import db


logger = logging.getLogger()


def find_all_by_code(code: str) -> List[Notice]:
    query_result = session.query(Notice)
    return query_result.filter_by(code=code).all()


def save_notices(notices: List[Notice]):
    push_target = defaultdict(list)
    for _notice in notices:
        notice, created = db.get_or_create(session, _notice, bid=_notice.bid)

        # created = True: DB에 저장된 같은 데이터가 없음 (Create)
        # created = False: DB에 저장된 같은 데이터가 있음 (Get)
        if created:
            push_target[notice.code].append(notice.title)
            logger.info(f"New data inserted! {notice.code}:{notice.title}")
            print(f"New data inserted! {notice.code}:{notice.title}")
        else:
            if notice.is_fixed != _notice.is_fixed:
                session.query(Notice).filter(Notice.bid == _notice.bid).update({'is_fixed': _notice.is_fixed})
    session.commit()
