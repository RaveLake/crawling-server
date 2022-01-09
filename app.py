import os
import sys
import threading

from flask import request

from src import app
from src.config.database import Session
from src.dto.request import NoticeRefreshRequest
from src.dto.response import get_200_response
from src.entity.Status import Status
from src.service.notice_service import crawling_notices


@app.route('/status', methods=('GET',))
def server_status():
    with Session.begin() as session:
        status = session.query(Status).first()
        return status.status


@app.route('/operation/refresh/notice', methods=('POST',))
def get_notices():
    requested_data = request.get_json()
    notice_refresh_request = NoticeRefreshRequest(
        all=requested_data.get('all'),
        targets=requested_data.get('targets'),
        page=requested_data.get('page'),
    )
    with Session.begin() as session:
        thread = threading.Thread(target=crawling_notices, args=(session, notice_refresh_request,))
        thread.start()

    return get_200_response(notice_refresh_request)


if __name__ == '__main__':
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    app.run(port=8080)
