from io import BytesIO
from fastapi import APIRouter, status, Response, File, UploadFile
from starlette.responses import StreamingResponse

from ewapi import CRUD
from ewapi.models import CreateProposalRequestModel, CreateProposalCommentRequestModel, FundingSourceRequestModel, \
    ProposalResponseModel, ProposalsListResponseModel, CreateEntityResponseModel
from ewapi.managers.proposals_manager import ProposalManager

router = APIRouter()


@router.get("/", response_model=ProposalsListResponseModel)
def get_proposals(response: Response):
    proposals = CRUD.proposals.get_proposals()
    if proposals:
        response.status_code = status.HTTP_200_OK
        return {"proposals": proposals}
    response.status_code = status.HTTP_404_NOT_FOUND


@router.get("/{proposal_id}", response_model=ProposalResponseModel)
def get_proposal(proposal_id: int, response: Response):
    proposal = CRUD.proposals.get_proposal(proposal_id)
    if proposal:
        response.status_code = status.HTTP_200_OK
        return proposal
    response.status_code = status.HTTP_404_NOT_FOUND


@router.post("/", response_model=CreateEntityResponseModel)
def create_proposal(r: CreateProposalRequestModel, response: Response):
    new_proposal_id = ProposalManager.send_proposal(r)
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


@router.get('/{proposal_id}/attachment')
def get_attachments(proposal_id: int):
    attachments = CRUD.attachments.get_attachments(proposal_id)
    return {"attachments": [{attachment.attachment_id: attachment.filename for attachment in attachments}]}


@router.post('/{proposal_id}/attachment')
async def add_attachment(proposal_id: int, file: UploadFile = File(...)):
    attachment_id = ProposalManager.send_attachment(proposal_id, file)
    return {"id": attachment_id}

  
@router.post("/{proposal_id}/funding_sources")
def create_funding_source(proposal_id: int, r: FundingSourceRequestModel, response: Response):
    ProposalManager.send_funding_source(proposal_id, r)
    response.status_code = status.HTTP_201_CREATED
    return {}
