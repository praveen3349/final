import sys
import os

# Adds the parent directory (which contains app.py) to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

def test_status():
    client = app.test_client()
    response = client.get('/status')
    assert response.status_code == 200
    assert response.json['status'] == 'running'
