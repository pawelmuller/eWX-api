from fastapi import APIRouter, status, Response
from api.utils.schemas import CreateUnitRequestModel

router = APIRouter()


@router.get("/")
def get_units(response: Response):
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"message": "Not implemented yet."}


@router.get("/{unit_id}")
def get_unit(unit_id: int, response: Response):
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"message": "Not implemented yet."}


@router.post("/")
def create_unit(request: CreateUnitRequestModel, response: Response):
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"message": "Not implemented yet."}
