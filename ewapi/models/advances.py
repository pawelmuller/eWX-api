from pydantic import Field, BaseModel


class AdvanceModel(BaseModel):
    amount: int \
        = Field(..., title="Advance amount",
                description="How much money will be requested for advance. "
                            "Warning: Use 1/1000000 of the usual amount, e.g. for 1,50 -> type 1500000")
    user_id: int \
        = Field(..., title="Advance recipient",
                description="ID of user, that will receive the advance")
