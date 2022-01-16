from contextlib import contextmanager

import sqlalchemy
from sqlalchemy.orm import sessionmaker

from src.config.config import DATABASE_URI

engine = sqlalchemy.create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
