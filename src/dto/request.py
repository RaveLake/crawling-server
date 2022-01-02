from dataclasses import dataclass
from typing import List


@dataclass
class NoticeRefreshRequest:
    targets: List[str]
    all: bool = False
    page: int = 1
