from ewapi.utils.db_connection import db_connect, get_next_id
from sqlalchemy import func
from ewapi.DTO import *
from ewapi.utils.decorators.catch_db_exceptions import catch_db_exceptions


def get_units() -> list:
    with get_session() as session:
        units = session.query(Unit).all()
    return units


def get_unit(unit_id: int) -> Unit:
    with get_session() as session:
        unit = session.query(Unit).where(Unit.unit_id == unit_id).first()
    return unit


@catch_db_exceptions
def create_unit(unit_type: str,
                name: str,
                description: str,
                chairperson_id: int,
                treasurer_id: int) -> (int, str):
    with get_session() as session:
        new_id = get_next_id(session, Unit.unit_id)
        new_unit = Unit(unit_id=new_id,
                        type=unit_type,
                        name=name,
                        description=description,
                        chairperson_id=chairperson_id,
                        treasurer_id=treasurer_id)
        session.add(new_unit)
        session.commit()
    return new_id, None


@catch_db_exceptions
def modify_unit(unit_id: int,
                unit_type: str,
                name: str,
                description: str,
                chairperson_id: int,
                treasurer_id: int) -> (bool, str):
    with get_session() as session:
        unit = session.query(Unit).where(Unit.unit_id == unit_id).first()
        unit.type = unit_type
        unit.name = name
        unit.description = description
        unit.chairperson_id = chairperson_id
        unit.treasurer_id = treasurer_id
        session.commit()
    return True, None
