from api.utils.db_connection import db_connect, get_next_id
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError
from api.DTO import *


def get_advances() -> list:
    with db_connect() as session:
        advances = session.query(Advance).all()
    return advances


def get_advance(advance_id: int) -> Advance:
    with db_connect() as session:
        advance = session.query(Advance).where(Advance.advance_id == advance_id).first()
    return advance


def create_advance(user_id: int,
                   proposal_id: int,
                   amount: int) -> (bool, str):
    with db_connect() as session:
        new_advance = Advance(recipient_id=user_id,
                              proposal_id=proposal_id,
                              amount=amount)
        session.add(new_advance)
        try:
            session.commit()
        except SQLAlchemyError as error:
            return False, str(error.__dict__['orig'])
    return True, None
