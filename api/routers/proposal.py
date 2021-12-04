from fastapi import APIRouter, status, Response
from api.utils.schemas import CreateProposalRequestModel, CreateProposalCommentRequestModel

router = APIRouter()


@router.get("/")
def get_proposals(response: Response):
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"message": "Not implemented yet."}


@router.get("/{proposal_id}")
def get_proposal(proposal_id: int, response: Response):
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"message": "Not implemented yet."}


@router.post("/")
def create_proposal(request: CreateProposalRequestModel, response: Response):
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"message": "Not implemented yet."}


@router.get("/{proposal_id}/comments")
def get_proposal_comments(proposal_id: int, response: Response):
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"message": "Not implemented yet."}


@router.post("/{proposal_id}/comments")
def create_proposal_comment(proposal_id: int, request: CreateProposalCommentRequestModel, response: Response):
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"message": "Not implemented yet."}
