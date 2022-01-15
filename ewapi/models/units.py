from pydantic import Field, BaseModel
from typing import Optional
from enum import Enum


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
    chairperson_id: int \
        = Field(..., title="Chairperson id",
                description="An ID of the user that will be assigned as a chairperson to the requested unit")
    treasurer_id: Optional[int] \
        = Field(None, title="Treasurer id",
                description="An ID of the user that will be assigned as a treasurer to the requested unit")


class UnitResponseModel(BaseModel):
    unit_id: int \
        = Field(..., title="Unit id",
                description="An ID of the unit")
    type: UnitType \
        = Field(..., title="Unit type",
                description="Unit type chosen from UnitType enumeration")
    name: str \
        = Field(..., title="Unit name",
                max_length=1000)
    description: Optional[str] \
        = Field("", title="Unit description",
                max_length=10000)
    chairperson_id: int \
        = Field(..., title="Chairperson id",
                description="An ID of the user that will be assigned as a chairperson to the requested unit")
    treasurer_id: Optional[int] \
        = Field(None, title="Treasurer id",
                description="An ID of the user that will be assigned as a treasurer to the requested unit")

    class Config:
        orm_mode = True


class UnitsListResponseModel(BaseModel):
    units: Optional[list[UnitResponseModel]] \
        = Field([], title="Units",
                description="A list of units described with UnitResponseModel")
