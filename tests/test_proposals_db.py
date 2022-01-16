import pytest
from sqlalchemy.exc import IntegrityError

from ewapi import CRUD
from ewapi.utils.db_connection import create_db_engine, get_session


class TestProposals:
    def test_add_proposal(self):
        create_db_engine(test=True)
        with get_session() as session:
            new_proposal_id = CRUD.proposals.create_proposal(session=session,
                                                             user_id=1,
                                                             name="TEST_PROPOSAL",
                                                             description="DESCRIPTION",
                                                             status_id=1)
            session.commit()
        assert CRUD.proposals.get_proposal(new_proposal_id).name == "TEST_PROPOSAL"
        assert CRUD.proposals.get_proposal(new_proposal_id).description == "DESCRIPTION"
        assert CRUD.proposals.get_proposal(new_proposal_id).status_id == 1

    def test_add_proposal_with_expenses(self):
        create_db_engine(test=True)
        with get_session() as session:
            new_proposal_id = CRUD.proposals.create_proposal(session=session,
                                                             user_id=1,
                                                             name="TEST_PROPOSAL",
                                                             description="DESCRIPTION",
                                                             status_id=1)

            new_expense_id_1 = CRUD.expenses.create_expense(session=session,
                                                            name="EXPENSE",
                                                            quantity=1,
                                                            price=100,
                                                            expense_type="TYPE",
                                                            proposal_id=new_proposal_id)

            new_expense_id_2 = CRUD.expenses.create_expense(session=session,
                                                            name="EXPENSE 2",
                                                            quantity=1,
                                                            price=100,
                                                            expense_type="TYPE",
                                                            proposal_id=new_proposal_id)
            session.commit()

        expenses = CRUD.proposals.get_proposal(new_proposal_id).expenses
        assert len(expenses) == 2
        assert expenses[0].name == "EXPENSE"
        assert expenses[1].name == "EXPENSE 2"

    def test_add_proposal_with_broken_expense(self):
        create_db_engine(test=True)
        with pytest.raises(IntegrityError):
            with get_session() as session:
                new_proposal_id = CRUD.proposals.create_proposal(session=session,
                                                                 user_id=1,
                                                                 name="TEST_PROPOSAL",
                                                                 description="DESCRIPTION",
                                                                 status_id=1)

                new_expense_id_1 = CRUD.expenses.create_expense(session=session,
                                                                name="EXPENSE",
                                                                quantity="QUANTITY",
                                                                price=100,
                                                                expense_type="TYPE",
                                                                proposal_id=new_proposal_id)
                session.commit()
        assert CRUD.proposals.get_proposal(new_proposal_id) is None
