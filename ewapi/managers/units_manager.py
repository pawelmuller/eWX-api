from ewapi.models import UnitResponseModel
from ewapi import CRUD


class UnitsManager(object):
    @classmethod
    def create_unit(cls, r: UnitResponseModel):
        new_unit_id, error_message = CRUD.units.create_unit(unit_type=r.type,
                                                            name=r.name,
                                                            description=r.description,
                                                            chairperson_id=r.chairperson_id,
                                                            treasurer_id=r.treasurer_id)
        return new_unit_id, error_message

    @classmethod
    def modify_unit(cls, unit_id: int, r: UnitResponseModel):
        is_successful, error_message = CRUD.units.modify_unit(unit_id=unit_id,
                                                              unit_type=r.type,
                                                              name=r.name,
                                                              description=r.description,
                                                              chairperson_id=r.chairperson_id,
                                                              treasurer_id=r.treasurer_id)
        return is_successful, error_message
