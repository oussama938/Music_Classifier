import pytest
from flask import Flask, jsonify
from vgg19_service.main import app
import warnings
from pathlib import Path
import base64


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_vgg19_audio_base64(client):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=DeprecationWarning)
        warnings.simplefilter("ignore", category=UserWarning)
        # audio_file_path = 'reggae1.wav'
        audio_file_path = Path(__file__).resolve().parent / 'reggae1.wav'
        with open(audio_file_path, 'rb') as audio_file:
            audio_data = audio_file.read()
        audio_data_base64 = base64.b64encode(audio_data).decode('utf-8')
        test_data = {'audio_data': audio_data_base64}

        response = client.post('/vgg19-base64', json=test_data)

        assert response.status_code == 200
