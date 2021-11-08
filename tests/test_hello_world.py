import unittest
from fastapi.testclient import TestClient
from api.main import app


class HelloWorldTest(unittest.TestCase):
    def test_hello(self):
        with TestClient(app) as client:
            response = client.get("/")
            assert response.status_code == 200
            assert response.json() == {"message": "Hello World"}
