from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "This is a Wikipedia API. Please call: /search or /wiki or /phrase"
    }

def test_read_phrase():
    response = client.get("/phrase/Beau Biden")
    assert response.status_code == 200
    assert response.json() == {
        "result": [
            "joseph robinette",
            "beau",
            "biden iii",
            "february",
            "may",
            "american politician",
            "army judge",
            "advocate",
            "general 's corps",
            "wilmington",
            "delaware",
            "u.s.",
            "joe biden",
            "neilia hunter biden",
            "44th attorney general",
            "delaware",
            "delaware",
            "national guard",
            "iraq",
            "brain cancer",
        ]
    }
