import pytest

def test_index(client):
    res = client.get("/health")
    assert res.status_code == 200
