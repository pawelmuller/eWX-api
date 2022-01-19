from io import BytesIO
from fastapi import APIRouter, status, Response, File, UploadFile
from starlette.responses import StreamingResponse

from ewapi import CRUD
from ewapi.models import CreateProposalRequestModel, CreateProposalCommentRequestModel, FundingSourceModel
from ewapi.utils.decorators.catch_db_exceptions import catch_db_exceptions
from ewapi.utils.db_connection import get_session

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


@router.get('/{proposal_id}/attachment/{attachment_id}')
def get_attachment(proposal_id: int, attachment_id: int):
    attachment = CRUD.attachments.get_attachment(proposal_id, attachment_id)
    return StreamingResponse(BytesIO(attachment.file_content))


@router.post('/{proposal_id}/attachment')
async def add_attachment(proposal_id: int, file: UploadFile = File(...)):
    file_content = await file.read()
    with get_session() as session:
        attachment_id = CRUD.attachments.create_attachment(session=session,
                                                           proposal_id=proposal_id,
                                                           filename=file.filename,
                                                           file_content=file_content)
        session.commit()
    return {"id": attachment_id}

  
@router.post("/{proposal_id}/funding_sources")
def create_funding_source(proposal_id: int, r: FundingSourceModel, response: Response):
    with get_session() as session:
        CRUD.funding_source.create_funding_source(session=session,
                                                  proposal_id=proposal_id,
                                                  amount=r.amount,
                                                  pool_id=r.pool_id)
        session.commit()
    response.status_code = status.HTTP_201_CREATED
    return {}
