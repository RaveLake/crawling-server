import sqlalchemy
from sqlalchemy.orm import sessionmaker

from config.develop_config import DATABASE_URI
from src.entity.BoardData import BoardData
from src.entity.Notice import Notice

engine = sqlalchemy.create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()


if __name__ == "__main__":
    notice = Notice(
        bid=0,
        code='test',
        is_fixed=False,
        title='test',
        link='test'
    )
    # session.add(notice)
    # session.commit()

    query_result = session.query(BoardData)
    bd: BoardData = query_result.filter_by(code='cse').first()
    print(bd.uri_root)
