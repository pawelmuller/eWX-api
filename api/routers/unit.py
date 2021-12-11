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
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"message": "Not implemented yet."}


@router.post("/")
def create_unit(r: CreateUnitRequestModel, response: Response):
    new_unit_id, error_message = CRUD.units.create_unit(unit_type=r.type,
                                                        name=r.name,
                                                        description=r.description,
                                                        chairperson_id=r.chairperson_id,
                                                        treasurer_id=r.treasurer_id)
    if new_unit_id:
        response.status_code = status.HTTP_201_CREATED
        return {"id": new_unit_id}
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error_message": error_message}
