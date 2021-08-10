"""Integration tests for app.py"""
from typing import Type
from flask.testing import FlaskClient
from flask.wrappers import Response
import pytest
import json

from bank_api.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()


def test_account_creation(client: FlaskClient):
    # Use the client to make requests e.g.:
    # client.post(...)
    # client.get(...)
    # https://flask.palletsprojects.com/en/1.1.x/testing/
    response_post = client.post("/accounts/jai")
    response_get = client.get("/accounts/jai")
    json_response = json.loads(response_get.data.decode())
    name = json_response['name']

    assert response_post.status_code == 200
    assert response_get.status_code == 200
    assert name == 'jai'

def test_add_funds(client: FlaskClient):
    response_post = client.post("/accounts/Jai")
    moneyargs = {'name': 'Jai',
                'amount': 25
                }
    response_post = client.post("/money", json=moneyargs)
    assert response_post.status_code == 200

    # We can go on to assert account balance is amount we posted
