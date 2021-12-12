from fastapi import APIRouter, status, Response
from api.utils.schemas import CreateProposalRequestModel, CreateProposalCommentRequestModel
from api import CRUD

router = APIRouter()


@router.get("/")
def get_proposals(response: Response):
    proposals = CRUD.proposals.get_proposals()
    if proposals:
        response.status_code = status.HTTP_200_OK
        return {"proposals": proposals}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND


@router.get("/{proposal_id}")
def get_proposal(proposal_id: int, response: Response):
    proposal = CRUD.proposals.get_proposal(proposal_id)
    if proposal:
        response.status_code = status.HTTP_200_OK
        return proposal
    else:
        response.status_code = status.HTTP_404_NOT_FOUND


@router.post("/")
def create_proposal(r: CreateProposalRequestModel, response: Response):
    new_proposal_id, error_message = CRUD.proposals.create_proposal(user_id=1,
                                                                    name=r.name,
                                                                    description=r.description,
                                                                    status_id=1)
    if new_proposal_id:
        for expense in r.expenses:
            new_expense_id, error_message = CRUD.expenses.create_expense(name=expense.name,
                                                                         quantity=expense.quantity,
                                                                         price=expense.price,
                                                                         expense_type=expense.type,
                                                                         proposal_id=new_proposal_id)
            if new_expense_id is None:
                response.status_code = status.HTTP_400_BAD_REQUEST
                return {"error_message": error_message}

        for advance in r.advances:
            is_successful, error_message = CRUD.advances.create_advance(user_id=1,
                                                                        proposal_id=new_proposal_id,
                                                                        amount=advance.amount)
            if is_successful is False:
                response.status_code = status.HTTP_400_BAD_REQUEST
                return {"error_message": error_message}
        response.status_code = status.HTTP_201_CREATED
        return {"id": new_proposal_id}

    response.status_code = status.HTTP_400_BAD_REQUEST
    return {"error_message": error_message}


@router.get("/{proposal_id}/comments")
def get_proposal_comments(proposal_id: int, response: Response):
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"message": "Not implemented yet."}


@router.post("/{proposal_id}/comments")
def create_proposal_comment(proposal_id: int, request: CreateProposalCommentRequestModel, response: Response):
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"message": "Not implemented yet."}
