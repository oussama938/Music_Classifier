from main import app
import pytest
from flask import Flask, jsonify


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_svm_endpoint(client):
    data = [[0.46562478, 0.08271162, 0.11577961, 0.0058971294, 3334.669316406379, 2148871.576233049, 2685.808816125656, 150566.88229063232, 6279.681075246711, 4723631.673790412, 0.21435546875, 0.027090743072050855, -0.0006625627, 0.006420883, 112.34714673913044, -117.59111, 5927.9683, 53.821686, 3263.619, 10.412251, 303.57928, 18.293306, 204.033, -0.030577581, 133.44731, 16.660912, 68.78127, -5.468606, 96.23146, 2.3087125, 56.62966, 2.9834719, 44.34068, 0.5670907, 36.846504, 0.05944262, 93.79759, -0.614988, 114.13315, -0.117973745, 58.886124, 3.0236957, 57.70551, -0.4565134, 36.777824, -0.7639519, 42.76433, -6.7437487, 31.674198, -1.3200325, 34.784958, -6.7639546, 35.680946, -0.85014516, 25.745037]]
    response = client.post('/svm', json=data)
    assert response.status_code == 200
    assert "Your music file type is" in response.get_data(as_text=True)
    predicted_label = response.get_data(as_text=True).split()[-1].strip('"')
    assert predicted_label == "disco"

