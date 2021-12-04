from pydantic import Field, BaseModel
from typing import Optional


class ExpenseModel(BaseModel):
    name: str \
        = Field(..., title="Expense name",
                max_length=100)
    type: str \
        = Field(..., title="Expense type",
                max_length=100)
    price: str \
        = Field(..., title="Expense price")
    quantity: float \
        = Field(..., title="Expense quantity")


class AdvanceModel(BaseModel):
    amount: str \
        = Field(..., title="Advance amount",
                description="How much money will be requested for advance")
    user_id: int \
        = Field(..., title="Advance recipient",
                description="ID of user, that will receive the advance")


class FundingSourcesModel(BaseModel):
    funding_source_id: int \
        = Field(..., title="Funding source id",
                description="An ID of the funding source that will be requested to cover the expenses")
    amount: str \
        = Field(..., title="Amount",
                description="How much money will be requested from a funding source")


class CreateProposalRequestModel(BaseModel):
    name: str \
        = Field(..., title="Proposal name",
                max_length=1000)
    description: Optional[str] \
        = Field("", title="Proposal description",
                max_length=10000)
    expenses: Optional[list[ExpenseModel]] \
        = Field([], title="Proposal expenses",
                description="A list of expenses described with dictionaries as an ExpenseModel")
    advances: Optional[list[AdvanceModel]] \
        = Field([], title="Proposal advances",
                description="A list of advances described with dictionaries as an AdvanceModel")
    funding_sources: Optional[list[FundingSourcesModel]] \
        = Field([], title="Proposal advances",
                description="A list of funding sources described with dictionaries as an FundingSourcesModel")


class CreateUnitRequestModel(BaseModel):
    type: str
    name: str
    description: str
    chairperson_id: Optional[int]
    treasurer_id: Optional[int]


class CreateProposalCommentRequestModel(BaseModel):
    content: str
