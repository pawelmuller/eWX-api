from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from api.utils.database_secrets import DB_VPN_URL, DB_LOGIN, DB_PASSWORD, DB_NAME
from api.DTO import *


def db_connect():
    engine = create_engine(f"postgresql://{DB_LOGIN}:{DB_PASSWORD}@{DB_VPN_URL}/{DB_NAME}", echo=False)
    Session = sessionmaker(engine)
    return Session()


def get_next_id(session, field):
    new_id = session.query(func.max(field)).scalar()
    if new_id is None:
        new_id = 1
    else:
        new_id += 1
    return new_id


def get_users():
    with db_connect() as session:
        users = session.query(User)
        return users


def get_proposals_by_status(status_id):
    with db_connect() as session:
        proposals = session.query(Proposal).where(Proposal.status_id==status_id)
        return proposals


def get_history_of_proposal(proposal_id):
    with db_connect() as session:
        history = session.query(StatusHistory).where(StatusHistory.proposal_id==proposal_id).order_by(StatusHistory.time)
        return history


# def create_proposal(user: User, reason: str, description=None):
#     return Proposal(None, user.user_id, reason, description)


def push_proposal_to_database(proposal: Proposal):
    with db_connect() as session:
        new_id = session.query(func.max(Proposal.proposal_id)).scalar() + 1
        proposal.proposal_id = new_id
        session.add(proposal)
        session.commit()


if __name__ == '__main__':
    user = get_users()[0]
    # proposal = create_proposal(user, "Powod")
    print(proposal)
    push_proposal_to_database(proposal)
