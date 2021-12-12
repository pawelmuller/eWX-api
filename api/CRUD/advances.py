from api.utils.db_connection import db_connect
from api.DTO import *
from api.utils.decorators.catch_db_exceptions import catch_db_exceptions


def get_advances() -> list:
    with db_connect() as session:
        advances = session.query(Advance).all()
    return advances


def get_advance(advance_id: int) -> Advance:
    with db_connect() as session:
        advance = session.query(Advance).where(Advance.advance_id == advance_id).first()
    return advance


@catch_db_exceptions
def create_advance(user_id: int,
                   proposal_id: int,
                   amount: int) -> (bool, str):
    with db_connect() as session:
        new_advance = Advance(recipient_id=user_id,
                              proposal_id=proposal_id,
                              amount=amount)
        session.add(new_advance)
        session.commit()
    return True, None
