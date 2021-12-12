from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from api.utils.database_secrets import DB_VPN_URL, DB_LOGIN, DB_PASSWORD, DB_NAME

active_session = None
engine = None


def get_session():
    global active_session
    global engine

    if active_session is None:
        Session = sessionmaker(engine)
        active_session = Session()
    return active_session


def create_db_engine(test: bool):
    global engine

    if test:
        engine = create_engine('sqlite:///..//tests//test.db', echo=False)
    else:
        engine = create_engine(f"postgresql://{DB_LOGIN}:{DB_PASSWORD}@{DB_VPN_URL}/{DB_NAME}", echo=False)


def get_next_id(session, field):
    new_id = session.query(func.max(field)).scalar()
    if new_id is None:
        new_id = 1
    else:
        new_id += 1
    return new_id
