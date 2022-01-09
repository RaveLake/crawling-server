from sqlalchemy import Column, Integer, String, Date, Boolean, BIGINT, DateTime, func

from src.entity import Base


class Status(Base):
    __tablename__ = 'status'
    status = Column(String(30), primary_key=True)
    modified_at = Column(DateTime, nullable=False)
