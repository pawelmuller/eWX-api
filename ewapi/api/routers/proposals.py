from fastapi import APIRouter, status, Response
from ewapi.models import CreateProposalRequestModel, CreateProposalCommentRequestModel
from ewapi import CRUD
from ewapi.utils.db_connection import db_connect
from ewapi.utils.decorators.catch_db_exceptions import catch_db_exceptions

router = APIRouter()


@router.get("/")
def get_proposals(response: Response):
    proposals = CRUD.proposals.get_proposals()
    if proposals:
        response.status_code = status.HTTP_200_OK
        return {"proposals": proposals}
    response.status_code = status.HTTP_404_NOT_FOUND


@router.get("/{proposal_id}")
def get_proposal(proposal_id: int, response: Response):
    proposal = CRUD.proposals.get_proposal(proposal_id)
    if proposal:
        response.status_code = status.HTTP_200_OK
        return proposal
    response.status_code = status.HTTP_404_NOT_FOUND


@router.post("/")
@catch_db_exceptions
def create_proposal(r: CreateProposalRequestModel, response: Response):
    with db_connect() as session:
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
    response.status_code = status.HTTP_201_CREATED
    return {"id": new_proposal_id}


@router.get("/{proposal_id}/comments")
def get_proposal_comments(proposal_id: int, response: Response):
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"message": "Not implemented yet."}


@router.post("/{proposal_id}/comments")
def create_proposal_comment(proposal_id: int, request: CreateProposalCommentRequestModel, response: Response):
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"message": "Not implemented yet."}
