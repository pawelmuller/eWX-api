from enum import Enum

from pydantic import Field, BaseModel
from typing import Optional


class ExpenseModel(BaseModel):
    name: str \
        = Field(..., title="Expense name",
                max_length=100)
    type: str \
        = Field(..., title="Expense type",
                max_length=100)
    price: int \
        = Field(..., title="Expense price",
                description="How much money does the expense cost. "
                            "Warning: Use 1/1000000 of the usual price, e.g. for 1,50 -> type 1500000")
    quantity: int \
        = Field(..., title="Expense quantity.",
                description="Warning: Use 1/1000 of the usual quantity, e.g. for 1,50 -> type 1500")


class AdvanceModel(BaseModel):
    amount: int \
        = Field(..., title="Advance amount",
                description="How much money will be requested for advance. "
                            "Warning: Use 1/1000000 of the usual amount, e.g. for 1,50 -> type 1500000")
    user_id: int \
        = Field(..., title="Advance recipient",
                description="ID of user, that will receive the advance")


class FundingSourcesModel(BaseModel):
    funding_source_id: int \
        = Field(..., title="Funding source id",
                description="An ID of the funding source that will be requested to cover the expenses")
    amount: int \
        = Field(..., title="Amount",
                description="How much money will be requested from a funding source. "
                            "Warning: Use 1/1000000 of the usual amount, e.g. for 1,50 -> type 1500000")


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


class UnitType(str, Enum):
    WRS = "WRS"
    RM = "RM"
    ORG = "ORG"
    KOM = "KOM"
    INNY = "INNY"


class CreateUnitRequestModel(BaseModel):
    type: UnitType \
        = Field(..., title="Unit type",
                description="Unit type chosen from UnitType enumeration")
    name: str \
        = Field(..., title="Unit name",
                max_length=1000)
    description: Optional[str] \
        = Field("", title="Unit description",
                max_length=10000)
    chairperson_id: Optional[int] \
        = Field(..., title="Chairperson id",
                description="An ID of the user that will be assigned as a chairperson to the requested unit")
    treasurer_id: Optional[int] \
        = Field(..., title="Treasurer id",
                description="An ID of the user that will be assigned as a treasurer to the requested unit")


class CreateProposalCommentRequestModel(BaseModel):
    content: str \
        = Field(..., title="Comment",
                max_length=10000)
