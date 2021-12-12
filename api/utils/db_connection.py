from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from api.utils.database_secrets import DB_VPN_URL, DB_LOGIN, DB_PASSWORD, DB_NAME

active_session = None


def get_session():
    if active_session is None:
        db_connect()
    return active_session


def db_connect(test=False):
    global active_session

    if test:
        engine = create_engine('sqlite:///..//tests//test.db', echo=False)
    else:
        engine = create_engine(f"postgresql://{DB_LOGIN}:{DB_PASSWORD}@{DB_VPN_URL}/{DB_NAME}", echo=False)

    Session = sessionmaker(engine)
    active_session = Session()


def get_next_id(session, field):
    new_id = session.query(func.max(field)).scalar()
    if new_id is None:
        new_id = 1
    else:
        new_id += 1
    return new_id
