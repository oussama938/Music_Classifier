import pytest
from flask import Flask
from front_service.main import app
from unittest.mock import Mock

class MockResponse:
    def __init__(self, text):
        self.text = text

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test():  
    assert 1==1 

# def test_classify_audio_svm(client, mocker):
#     # Mock the request to svm_service
#     mocker.patch('requests.post', return_value=MockResponse("Your music file type is label_svm"))

#     # Prepare data to send in the request
#     data = {
#         # Your JSON data structure here
#     }

#     # Make a request to the front_service endpoint that communicates with svm_service
#     response = client.post('/classify', json=data)

#     # Assert the response from the front_service endpoint
#     assert response.status_code == 200
#     assert "Your music file type is" in response.get_data(as_text=True)
#     predicted_label = response.get_data(as_text=True).split()[-1].strip('"')
#     assert predicted_label == "label_svm"

# def test_classify_audio_vgg(client, mocker):
#     mocker.patch('requests.post', return_value=MockResponse("Your music file type is label_vgg"))
#     response = client.post('/classify', data={'file': 'audio_data', 'model_selected': 'vgg'})
    
#     assert response.status_code == 200
#     assert "Your music file type is label_vgg" in response.get_data(as_text=True)

# def test_classify_audio_none(client):
#     response = client.post('/classify', data={'file': 'audio_data', 'model_selected': 'none'})
#     assert response.status_code == 200
