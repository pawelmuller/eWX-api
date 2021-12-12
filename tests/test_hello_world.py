import unittest
from fastapi.testclient import TestClient
import api.main as main


class HelloWorldTest(unittest.TestCase):
    def test_hello(self):
        with TestClient(main.app) as client:
            response = client.get("/")
            assert response.status_code == 200
            assert response.json() == {"message": "Hello World"}
