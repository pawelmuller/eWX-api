from ewapi.utils.db_connection import get_session
from ewapi.models import CreateProposalRequestModel, FundingSourceRequestModel

from ewapi import CRUD
from ewapi.utils.decorators.catch_db_exceptions import catch_db_exceptions
from fastapi import File, UploadFile


class ProposalManager(object):
    @classmethod
    @catch_db_exceptions
    def send_proposal(cls, r: CreateProposalRequestModel):
        with get_session() as session:
            new_proposal_id = CRUD.proposals.create_proposal(session=session,
                                                             user_id=1,
                                                             name=r.name,
                                                             description=r.description,
                                                             status_id=1)
            for expense in r.expenses:
                new_expense_id = CRUD.expenses.create_expense(session=session,
                                                              name=expense.name,
                                                              quantity=expense.quantity,
                                                              price=expense.price,
                                                              expense_type=expense.type,
                                                              proposal_id=new_proposal_id)

            for advance in r.advances:
                CRUD.advances.create_advance(session=session,
                                             user_id=advance.user_id,
                                             proposal_id=new_proposal_id,
                                             amount=advance.amount)
            session.commit()
        return new_proposal_id

    @classmethod
    async def send_attachment(cls, proposal_id: int, file: UploadFile = File(...)):
        file_content = await file.read()
        with get_session() as session:
            attachment_id = CRUD.attachments.create_attachment(session=session,
                                                               proposal_id=proposal_id,
                                                               filename=file.filename,
                                                               file_content=file_content)
            session.commit()
        return attachment_id

    @classmethod
    def send_funding_source(cls, proposal_id: int, r: FundingSourceRequestModel):
        with get_session() as session:
            CRUD.funding_sources.create_funding_source(session=session,
                                                       proposal_id=proposal_id,
                                                       amount=r.amount,
                                                       pool_id=r.pool_id)
            session.commit()

