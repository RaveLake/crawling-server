from src.dto.request import NoticeRefreshRequest
from src.service.crawling_service import crawling_task


def crawling_notices(request: NoticeRefreshRequest):
    if request.all:
        pass
    targets = request.targets

    for target in targets:
        result = crawling_task(request.page, target)
        print(result)
