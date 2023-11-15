from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_top_players():
    response = client.get("/top-players")
    assert response.status_code == 200

# Add more tests for other endpoints
