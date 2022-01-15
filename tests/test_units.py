from fastapi.testclient import TestClient
import ewapi.api.main as main


class TestUnits:
    def test_correct_unit_type(self):
        types = ["XYZ", "A"]
        with TestClient(main.app) as client:
            for entry in types:
                request = {
                    "type": entry,
                    "name": "Test name",
                    "description": "Test description",
                    "chairperson_id": 10
                }
                response = client.post("/unit/", json=request)
                assert response.status_code == 422

    def test_name_length(self):
        with TestClient(main.app) as client:
            request = {
                "type": "ORG",
                "name": "Test name" * 2500,
                "description": "Test description",
                "chairperson_id": 10
            }
            response = client.post("/unit/", json=request)
            assert response.status_code == 422

    def test_description_length(self):
        with TestClient(main.app) as client:
            request = {
                "type": "ORG",
                "name": "Test name",
                "description": "Test description" * 5000,
                "chairperson_id": 10
            }
            response = client.post("/unit/", json=request)
            assert response.status_code == 422
