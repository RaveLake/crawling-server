from typing import Dict, List

from src.entity.Notice import Notice


def __get_fixed(is_fixed):
    return True if is_fixed and not is_fixed.isdigit() else False


def __null_if_blank(_param: str):
    param = _param.strip()
    return param if param != '' else None


def to_notice_entity(notices: List[Dict]):
    return [
        Notice(
            bid=notice['bid'],
            code=notice['code'],
            is_fixed=__get_fixed(notice['is_fixed']),
            title=notice['title'],
            link=notice['title'],
            date=__null_if_blank(notice['date']),
            author=__null_if_blank(notice['author']),
            reference=__null_if_blank(notice['reference']),
        ) for notice in notices
    ]
