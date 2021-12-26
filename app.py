from flask import Flask, request

from src.dto.request import NoticeRefreshRequest
from src.dto.response import get_200_response
from src.service.notice_service import crawling_notices

app = Flask(__name__)


@app.route('/operation/refresh/notice', methods=('POST',))
def get_notices():
    requested_data = request.get_json()
    notice_refresh_request = NoticeRefreshRequest(
        all=requested_data.get('all'),
        targets=requested_data.get('targets'),
    )
    crawling_notices(notice_refresh_request)

    return get_200_response(notice_refresh_request)


if __name__ == '__main__':
    app.run()
