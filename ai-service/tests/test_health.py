import os

from fastapi.testclient import TestClient
from main import APP_TITLE, app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert "env" in body


def test_app_title_is_configurable():
    expected = os.environ.get("APP_TITLE", "AI Factcheck Enterprise - AI Service")
    assert APP_TITLE == expected
