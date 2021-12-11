from api.utils.db_connection import db_connect
from api.DTO import *


def get_units() -> list:
    with db_connect() as session:
        units = session.query(Unit).all()
    return units


def create_unit():
    pass
