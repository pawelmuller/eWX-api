from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from api.utils.database_secrets import DB_VPN_URL, DB_LOGIN, DB_PASSWORD, DB_NAME


def db_connect():
    engine = create_engine(f"postgresql://{DB_LOGIN}:{DB_PASSWORD}@{DB_VPN_URL}/{DB_NAME}", echo=False)
    Session = sessionmaker(engine)
    return Session()


def get_next_id(session, field):
    new_id = session.query(func.max(field)).scalar()
    if new_id is None:
        new_id = 1
    else:
        new_id += 1
    return new_id
