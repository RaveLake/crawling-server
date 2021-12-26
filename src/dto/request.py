from dataclasses import dataclass
from typing import List


@dataclass
class NoticeRefreshRequest:
    targets: List
    all: bool = False
    page: int = 1
