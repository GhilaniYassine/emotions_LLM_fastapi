import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_analyze_emotions():
    response = client.post("/analyze", json={"text": "I feel happy and excited!"})
    assert response.status_code == 200
    assert "Joy" in response.json()
    assert response.json()["Joy"] == "+"

def test_analyze_emotions_negative():
    response = client.post("/analyze", json={"text": "I am feeling very sad and hopeless."})
    assert response.status_code == 200
    assert "Sadness" in response.json()
    assert response.json()["Sadness"] == "+"
    assert "Joy" in response.json()
    assert response.json()["Joy"] == "-"

def test_analyze_emotions_empty():
    response = client.post("/analyze", json={"text": ""})
    assert response.status_code == 400
    assert response.json() == {"detail": "Text input cannot be empty."}