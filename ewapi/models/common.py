from pydantic import Field, BaseModel


class CreateEntityResponseModel(BaseModel):
    id: int \
        = Field(..., title="Entity id",
                description="An ID of the created entity")
