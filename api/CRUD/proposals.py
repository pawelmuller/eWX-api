from api.utils.db_connection import db_connect, get_next_id
from api.DTO import *
from api.utils.decorators.catch_db_exceptions import catch_db_exceptions


def get_proposals() -> list:
    with db_connect() as session:
        proposals = session.query(Proposal).all()
    return proposals


def get_proposal(proposal_id: int) -> Proposal:
    with db_connect() as session:
        proposal = session.query(Proposal).where(Proposal.proposal_id == proposal_id).first()
    return proposal


@catch_db_exceptions
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
        session.commit()
    return new_id, None
