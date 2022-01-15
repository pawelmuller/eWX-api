from fastapi import APIRouter, status, Response
from ewapi.models import CreateUnitRequestModel, UnitResponseModel, UnitsListResponseModel, CreateEntityResponseModel
from ewapi import CRUD

router = APIRouter()


@router.get("/", response_model=UnitsListResponseModel)
def get_units(response: Response):
    units = CRUD.units.get_units()
    if units:
        response.status_code = status.HTTP_200_OK
        return {"units": units}
    response.status_code = status.HTTP_404_NOT_FOUND


@router.get("/{unit_id}", response_model=UnitResponseModel)
def get_unit(unit_id: int, response: Response):
    unit = CRUD.units.get_unit(unit_id)
    if unit:
        response.status_code = status.HTTP_200_OK
        return unit
    response.status_code = status.HTTP_404_NOT_FOUND


@router.post("/", response_model=CreateEntityResponseModel)
def create_unit(r: CreateUnitRequestModel, response: Response):
    new_unit_id, error_message = CRUD.units.create_unit(unit_type=r.type,
                                                        name=r.name,
                                                        description=r.description,
                                                        chairperson_id=r.chairperson_id,
                                                        treasurer_id=r.treasurer_id)
    if new_unit_id:
        response.status_code = status.HTTP_201_CREATED
        return {"id": new_unit_id}
    response.status_code = status.HTTP_400_BAD_REQUEST


@router.put("/{unit_id}")
def modify_unit(unit_id: int, r: CreateUnitRequestModel, response: Response):
    is_successful, error_message = CRUD.units.modify_unit(unit_id=unit_id,
                                                          unit_type=r.type,
                                                          name=r.name,
                                                          description=r.description,
                                                          chairperson_id=r.chairperson_id,
                                                          treasurer_id=r.treasurer_id)
    if is_successful:
        response.status_code = status.HTTP_200_OK
        return
    response.status_code = status.HTTP_400_BAD_REQUEST