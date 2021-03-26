import pytest

def test_all(client, captured_templates):
    res = client.get('/')
    assert res.status_code == 200
    template, context = captured_templates[0]
    assert template.name == "home.html"
    assert context.get("type", None) == None

def test_recepie(client, captured_templates):
    res = client.get('/recepie')
    assert res.status_code  == 200
    template, context = captured_templates[0]
    assert template.name  == "home.html"
    assert context["context"]["type"] == "recepie"
    assert context["context"]["entries"][0]["link"] == "/recepie/0"

def test_ingredient(client, captured_templates):
    res = client.get('/ingredient')
    assert res.status_code  == 200
    template, context = captured_templates[0]
    assert template.name  == "home.html"
    assert context["context"]["type"] == "ingredient"
    assert context["context"]["entries"][0]["link"] == "/ingredient/0"

