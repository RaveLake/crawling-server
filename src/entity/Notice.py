from sqlalchemy import Column, Integer, String, Date, Boolean, BIGINT, DateTime, func

from src.entity import Base


class Notice(Base):
    __tablename__ = 'notice'
    id = Column(BIGINT, primary_key=True)
    bid = Column(BIGINT)
    code = Column(String(30))
    is_fixed = Column(Boolean, default=False)
    title = Column(String(100))
    link = Column(String(500))
    date = Column(Date, nullable=True)
    author = Column(String(30), nullable=True)
    reference = Column(String(50), nullable=True)
    created_at = Column(DateTime, default=func.sysdate())

    # __mapper_args__ = {
    #     "order_by": (is_fixed.desc(), date.desc())
    # }

    def __init__(self, bid, code, is_fixed, title, link, date=None, author=None, reference=None, created_at=None):
        self.bid = bid
        self.code = code
        self.is_fixed = is_fixed
        self.title = title
        self.link = link
        self.date = date
        self.author = author
        self.reference = reference
        self.created_at = created_at

    def __str__(self):
        return self.title
