from fastapi.testclient import TestClient
# Adding a relative path in the directory for detecting the api module
import sys
sys.path.append(".")

from api.main import app

client = TestClient(app)
# Sample test for github actions
def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message":"Hello from AWS Lambda!"}
