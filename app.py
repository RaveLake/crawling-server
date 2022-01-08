import os
import sys

from flask import request

from src import app
from src.dto.request import NoticeRefreshRequest
from src.dto.response import get_200_response
from src.service.notice_service import crawling_notices


@app.route('/operation/refresh/notice', methods=('POST',))
def get_notices():
    requested_data = request.get_json()
    notice_refresh_request = NoticeRefreshRequest(
        all=requested_data.get('all'),
        targets=requested_data.get('targets'),
        page=requested_data.get('page'),
    )
    crawling_notices(notice_refresh_request)

    return get_200_response(notice_refresh_request)


if __name__ == '__main__':
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    app.run(port=8080)
