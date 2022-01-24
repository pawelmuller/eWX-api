from ewapi import CRUD
from ewapi.utils.db_connection import create_db_engine, get_session


class TestFundingSource:
    def test_link_pools(self):
        create_db_engine(test=True)
        with get_session() as session:
            new_proposal_id = CRUD.proposals.create_proposal(session=session,
                                                             user_id=1,
                                                             name="TEST_PROPOSAL",
                                                             description="DESCRIPTION",
                                                             status_id=1)

            CRUD.funding_sources.create_funding_source(session=session,
                                                       pool_id=1,
                                                       proposal_id=new_proposal_id,
                                                       amount=100)

            CRUD.funding_sources.create_funding_source(session=session,
                                                       pool_id=2,
                                                       proposal_id=new_proposal_id,
                                                       amount=100)
            session.commit()
        funding_sources = CRUD.proposals.get_proposal(new_proposal_id).funding_sources
        assert len(funding_sources) == 2
        assert funding_sources[0].pool_id == 1
        assert funding_sources[0].amount == 100
        assert funding_sources[1].pool_id == 2
        assert funding_sources[1].amount == 100
