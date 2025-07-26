import os
import sys

# Add root project path to sys.path for importing app.py
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)

from app import app  # noqa: E402


def test_status():
    client = app.test_client()
    response = client.get('/status')
    assert response.status_code == 200
    assert response.json['status'] == 'running'
