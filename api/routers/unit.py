from fastapi import APIRouter, status, Response
from api.utils.schemas import CreateUnitRequestModel
from api import CRUD

router = APIRouter()


@router.get("/")
def get_units(response: Response):
    units = CRUD.units.get_units()
    if units:
        response.status_code = status.HTTP_200_OK
        return {"units": units}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return


@router.get("/{unit_id}")
def get_unit(unit_id: int, response: Response):
    units = CRUD.units.get_unit(unit_id)
    if units:
        response.status_code = status.HTTP_200_OK
        return units
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return


@router.post("/")
def create_unit(request: CreateUnitRequestModel, response: Response):
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"message": "Not implemented yet."}
