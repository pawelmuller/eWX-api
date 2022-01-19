from ewapi.utils.db_connection import get_session
from ewapi.DTO import *


def get_funding_sources() -> list:
    with get_session() as session:
        funding_sources = session.query(FundingSource).all()
    return funding_sources


def get_funding_source(proposal_id: int, pool_id: int) -> FundingSource:
    with get_session() as session:
        funding_source = session.query(FundingSource).where(
            FundingSource.proposal_id == proposal_id, FundingSource.pool_id == pool_id
        ).first()
    return funding_source


def create_funding_source(session,
                          pool_id: int,
                          proposal_id: int,
                          amount: int):
    new_funding_source = FundingSource(pool_id=pool_id,
                                       proposal_id=proposal_id,
                                       amount=amount)
    session.add(new_funding_source)
