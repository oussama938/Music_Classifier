from svm_service.main import app
import pytest
from flask import Flask, jsonify
import warnings
import base64
from pathlib import Path

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_svm_audio_base64(client):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=DeprecationWarning)
        warnings.simplefilter("ignore", category=UserWarning)
        # audio_file_path = 'reggae1.wav'
        audio_file_path = Path(__file__).resolve().parent / 'reggae1.wav'
        with open(audio_file_path, 'rb') as audio_file:
            audio_data = audio_file.read()
        audio_data_base64 = base64.b64encode(audio_data).decode('utf-8')
        test_data = {'audio_data': audio_data_base64}

        response = client.post('/svm-base64', json=test_data)

        assert response.status_code == 200


# def test_svm_endpoint(client):
#     with warnings.catch_warnings():
#         warnings.simplefilter("ignore", category=DeprecationWarning)
#         warnings.simplefilter("ignore", category=UserWarning)
#         data = [[0.3935568332672119, 0.09074261784553528, 0.08854293823242188, 0.002194312633946538, 1969.2642763252888, 682612.2704996889, 2002.4552547562073, 307143.65445310064, 4142.941128250456, 3187357.327405706, 0.10453495666058395, 0.005576264160227793, -6.631491123698652e-05, 0.006799723487347364, 151.99908088235293, -204.54766845703125, 6055.77099609375, 106.23225402832031, 1292.43505859375, -27.95388412475586, 1028.65185546875, 42.14997100830078, 406.9546813964844, 9.0360746383667, 293.560791015625, 25.09910774230957, 216.4720001220703, -2.0812034606933594, 259.67822265625, 18.512313842773438, 190.85289001464844, -5.8915815353393555, 94.83415985107422, 17.04735565185547, 90.60223388671875, -13.884904861450195, 97.03601837158203, 10.422618865966797, 96.95103454589844, -5.226133823394775, 89.58555603027344, 1.669304370880127, 134.73367309570312, 1.879082202911377, 92.24433898925781, 4.162893295288086, 87.39179229736328, -6.827472686767578, 44.8297004699707, -1.0497223138809204, 26.921979904174805, -6.895261764526367, 39.83046340942383, -5.516641616821289, 47.29544448852539]]
#         response = client.post('/svm', json=data)
#         assert response.status_code == 200
#         assert "Your music file type is" in response.get_data(as_text=True)
#         predicted_label = response.get_data(as_text=True).split()[-1].strip('"')
#         assert predicted_label == "reggae"