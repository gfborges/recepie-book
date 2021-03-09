import pytest

def test_index(client, captured_templates):
    res = client.get('/')
    assert res.status_code == 200
    template, context = captured_templates[0]
    assert template.name == "index.html"
