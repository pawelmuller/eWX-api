from api.utils.db_connection import db_connect
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError
from api.DTO import *


def get_units() -> list:
    with db_connect() as session:
        units = session.query(Unit).all()
    return units


def get_unit(unit_id: int) -> Unit:
    with db_connect() as session:
        unit = session.query(Unit).where(Unit.unit_id == unit_id).first()
    return unit


def create_unit(unit_type: str,
                name: str,
                description: str,
                chairperson_id: int,
                treasurer_id: int) -> (int, str):
    with db_connect() as session:
        new_id = session.query(func.max(Unit.unit_id)).scalar() + 1
        new_unit = Unit(unit_id=new_id,
                        type=unit_type,
                        name=name,
                        description=description,
                        chairperson_id=chairperson_id,
                        treasurer_id=treasurer_id)
        session.add(new_unit)
        try:
            session.commit()
        except SQLAlchemyError as error:
            return None, str(error.__dict__['orig'])
    return new_id, None


def modify_unit(unit_id: int,
                unit_type: str,
                name: str,
                description: str,
                chairperson_id: int,
                treasurer_id: int) -> (bool, str):
    with db_connect() as session:
        unit = session.query(Unit).where(Unit.unit_id == unit_id).first()
        unit.type = unit_type
        unit.name = name
        unit.description = description
        unit.chairperson_id = chairperson_id
        unit.treasurer_id = treasurer_id
        try:
            session.commit()
        except SQLAlchemyError as error:
            return False, str(error.__dict__['orig'])
    return True, None
