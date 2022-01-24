from pydantic import Field, BaseModel
from typing import Optional

from ewapi.models import AdvanceRequestModel, ExpenseRequestModel, ExpenseResponseModel, FundingSourceRequestModel, \
    AdvanceResponseModel, FundingSourceResponseModel


class CreateProposalRequestModel(BaseModel):
    name: str \
        = Field(..., title="Proposal name",
                max_length=1000)
    description: Optional[str] \
        = Field("", title="Proposal description",
                max_length=10000)
    expenses: Optional[list[ExpenseRequestModel]] \
        = Field([], title="Proposal expenses",
                description="A list of expenses described with dictionaries as an ExpenseModel")
    advances: Optional[list[AdvanceRequestModel]] \
        = Field([], title="Proposal advances",
                description="A list of advances described with dictionaries as an AdvanceModel")
    funding_sources: Optional[list[FundingSourceRequestModel]] \
        = Field([], title="Proposal advances",
                description="A list of funding sources described with dictionaries as an FundingSourcesModel")


class CreateProposalCommentRequestModel(BaseModel):
    content: str \
        = Field(..., title="Comment",
                max_length=10000)


class ProposalResponseModel(BaseModel):
    proposal_id: int \
        = Field(..., title="Proposal id",
                description="An ID of the proposal")
    name: str \
        = Field(..., title="Proposal name",
                max_length=1000)
    description: Optional[str] \
        = Field("", title="Proposal description",
                max_length=10000)
    expenses: Optional[list[ExpenseResponseModel]] \
        = Field([], title="Proposal expenses",
                description="A list of expenses described with dictionaries as an ExpenseModel")
    advances: Optional[list[AdvanceResponseModel]] \
        = Field([], title="Proposal advances",
                description="A list of advances described with dictionaries as an AdvanceModel")
    funding_sources: Optional[list[FundingSourceResponseModel]] \
        = Field([], title="Proposal advances",
                description="A list of funding sources described with dictionaries as an FundingSourcesModel")

    class Config:
        orm_mode = True


class ProposalsListResponseModel(BaseModel):
    proposals: Optional[list[ProposalResponseModel]] \
        = Field([], title="Proposals",
                description="A list of proposals described with ProposalResponseModel")
