from ewapi.utils.db_connection import get_session
from ewapi.DTO import *


def get_advances() -> list:
    with get_session() as session:
        advances = session.query(Advance).all()
    return advances


def get_advance(advance_id: int) -> Advance:
    with get_session() as session:
        advance = session.query(Advance).where(Advance.advance_id == advance_id).first()
    return advance


def create_advance(session,
                   user_id: int,
                   proposal_id: int,
                   amount: int) -> None:
    new_advance = Advance(recipient_id=user_id,
                          proposal_id=proposal_id,
                          amount=amount)
    session.add(new_advance)
