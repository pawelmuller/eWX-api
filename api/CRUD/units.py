from api.utils.db_connection import db_connect
from api.DTO import *


def get_units() -> list:
    with db_connect() as session:
        units = session.query(Unit).all()
    return units


def get_unit(unit_id: int) -> Unit:
    with db_connect() as session:
        unit = session.query(Unit).where(Unit.unit_id == unit_id).first()
    return unit


def create_unit():
    pass
