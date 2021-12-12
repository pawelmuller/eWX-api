from api.CRUD.units import create_unit, get_unit, modify_unit


class TestUnits:
    def test_add_unit_good(self):
        unit_id, error_message = create_unit(unit_type='WRS',
                                             name='Test',
                                             description='Description',
                                             chairperson_id=1,
                                             treasurer_id=1)
        unit = get_unit(unit_id)
        assert unit.type == 'WRS'
        assert unit.name == 'Test'
        assert unit.description == 'Description'
        assert unit.chairperson_id == 1
        assert unit.treasurer_id == 1

    def test_modify_unit(self):
        unit_id, error_message = create_unit(unit_type='WRS',
                                             name='Test',
                                             description='Description',
                                             chairperson_id=1,
                                             treasurer_id=1)
        unit = get_unit(unit_id)
        assert unit.name == 'Test'

        modify_unit(unit_id=unit_id,
                    unit_type='WRS',
                    name='Test after change',
                    description='Description',
                    chairperson_id=1,
                    treasurer_id=1)

        unit = get_unit(unit_id)
        assert unit.name == 'Test after change'
