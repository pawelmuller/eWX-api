from api.utils.db_connection import db_connect, get_next_id
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError
from api.DTO import *


def get_proposals() -> list:
    with db_connect() as session:
        proposals = session.query(Proposal).all()
    return proposals


def get_proposal(proposal_id: int) -> Proposal:
    with db_connect() as session:
        proposal = session.query(Proposal).where(Proposal.proposal_id == proposal_id).first()
    return proposal


def create_proposal(user_id: int,
                    name: str,
                    description: str,
                    status_id: int) -> (int, str):
    with db_connect() as session:
        new_id = get_next_id(session, Proposal.proposal_id)
        new_proposal = Proposal(proposal_id=new_id,
                                user_id=user_id,
                                name=name,
                                description=description,
                                status_id=status_id)
        session.add(new_proposal)
        try:
            session.commit()
        except SQLAlchemyError as error:
            return None, str(error.__dict__['orig'])
    return new_id, None
