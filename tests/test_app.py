import pytest
import sys
import os
import json

# E501: line too long - Broken into multiple lines for readability
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)
from app import app  # noqa: E402


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Flask API Dashboard" in response.data


def test_status_page_html(client):
    response = client.get('/status')
    assert response.status_code == 200
    assert b"API Status: Healthy" in response.data


def test_status_page_json(client):
    response = client.get('/status?json=true')
    assert response.status_code == 200
    assert response.mimetype == 'application/json'

    data = json.loads(response.data)
    assert data['status'] == 'healthy'
    assert 'last_updated' in data
