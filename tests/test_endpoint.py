from app import create_app
import json


def test_config():
    assert create_app({"TESTING": True}).testing


def test_get_time(client):
    rv = client.get("/api/time")
    assert "time" in json.loads(rv.data)
