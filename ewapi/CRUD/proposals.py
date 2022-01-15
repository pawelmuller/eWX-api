from ewapi.utils.db_connection import get_next_id
from ewapi.DTO import *
from ewapi.utils.db_connection import get_session


def get_proposals() -> list:
    with get_session() as session:
        proposals = session.query(Proposal).all()
    return proposals


def get_proposal(proposal_id: int) -> Proposal:
    with get_session() as session:
        proposal = session.query(Proposal).where(Proposal.proposal_id == proposal_id).first()
    return proposal


def create_proposal(session,
                    user_id: int,
                    name: str,
                    description: str,
                    status_id: int) -> (int, str):
    new_id = get_next_id(session, Proposal.proposal_id)
    new_proposal = Proposal(proposal_id=new_id,
                            user_id=user_id,
                            name=name,
                            description=description,
                            status_id=status_id)
    session.add(new_proposal)
    return new_id
