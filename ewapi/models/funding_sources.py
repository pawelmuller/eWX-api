from pydantic import Field, BaseModel


class FundingSourcesModel(BaseModel):
    funding_source_id: int \
        = Field(..., title="Funding source id",
                description="An ID of the funding source that will be requested to cover the expenses")
    amount: int \
        = Field(..., title="Amount",
                description="How much money will be requested from a funding source. "
                            "Warning: Use 1/1000000 of the usual amount, e.g. for 1,50 -> type 1500000")