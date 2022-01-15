from pydantic import Field, BaseModel


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
