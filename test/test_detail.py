import pytest

def test_recepie_detail(client, captured_templates):
    res = client.get("/recepie/0")
    template, context = captured_templates[0]
    assert template.name == "detail.html"
    assert context["context"]["name"] == "Macarrão"

def test_recepie_detail(client, captured_templates):
    res = client.get("/ingredient/0")
    template, context = captured_templates[0]
    assert template.name == "detail.html"
    assert context["context"]["name"] == "limão"