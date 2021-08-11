# app/tests/test_foo.py
import json

from django.urls import reverse


def test_hello_world():
    assert "hello_world" == "hello_world"
    assert "foo" != "bar"


def test_ping(client, settings):
    settings.SECURE_SSL_REDIRECT = False
    url = reverse("ping")
    response = client.get(url)
    content = json.loads(response.content)
    assert response.status_code == 200
    assert content["ping"] == "pong"
