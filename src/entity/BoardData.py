from sqlalchemy import Column, Integer, String, Date, Boolean, BIGINT

from src.entity import Base


class BoardData(Base):
    __tablename__ = 'board_data'
    id = Column(BIGINT, primary_key=True)
    crawling_status = Column(String(2))
    code = Column(String(30), unique=True)
    path = Column(String(30))
    name = Column(String(30))
    uri_root = Column(String(500))
    model_name = Column(String(30))
    key_name_bid = Column(String(30))
    key_name_page = Column(String(30), nullable=True)
    uri_is_fixed = Column(String(500))
    uri_link = Column(String(500))
    uri_title = Column(String(500))
    uri_date = Column(String(500), nullable=True)
    uri_author = Column(String(500), nullable=True)
    uri_reference = Column(String(500), nullable=True)
    uri_inside_date = Column(String(500), nullable=True)
    notice_drop_num = Column(Integer, nullable=True)

    def __init__(
            self,
            code,
            path,
            name,
            uri_root,
            model_name,
            key_name_bid,
            uri_is_fixed,
            uri_link,
            uri_title,
            crawling_status='00',
            key_name_page=None,
            uri_date=None,
            uri_author=None,
            uri_reference=None,
            uri_inside_date=None,
            notice_drop_num=None,
    ):
        self.crawling_status = crawling_status
        self.code = code
        self.path = path
        self.name = name
        self.uri_root = uri_root
        self.model_name = model_name
        self.key_name_bid = key_name_bid
        self.key_name_page = key_name_page
        self.uri_is_fixed = uri_is_fixed
        self.uri_link = uri_link
        self.uri_title = uri_title
        self.uri_date = uri_date
        self.uri_author = uri_author
        self.uri_reference = uri_reference
        self.uri_inside_date = uri_inside_date
        self.notice_drop_num = notice_drop_num

    def __str__(self):
        return self.name + "-" + self.code
