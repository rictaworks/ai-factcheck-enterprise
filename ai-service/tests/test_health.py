import pathlib

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert "env" in body


def test_no_hardcoded_title():
    src = (pathlib.Path(__file__).parent.parent / "main.py").read_text()
    assert "AI Factcheck Enterprise" not in src
