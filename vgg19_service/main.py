
from flask import Flask, request, jsonify,render_template
import os
import pickle
import joblib

import numpy as np
import librosa
from sklearn.preprocessing import StandardScaler

import io
import base64

# tensorflow==2.14.0
# Keras==2.7.0
# Pillow==8.4.0


app = Flask(__name__,static_url_path='/static')

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Adjust as needed
app.config['UPLOAD_FOLDER'] = '../upload'
file_name = 'Vgg19Keras.pkl'

# Get the current working directory
current_directory = os.path.dirname(os.path.abspath(__file__))
# Create the full file path
file_path = os.path.join(current_directory, file_name)
# Load the content of the file using joblib
model = joblib.load(file_path)

# Create the full file path
file_path = os.path.join(current_directory, 'standard_scaler.pkl')
# Load the content of the file using joblib
scaler = joblib.load(file_path)

@app.route('/vgg19-base64', methods=['POST'])
def process_predict_audio():
     if request.method == 'POST':
          try:
               audio_data_base64 = request.json.get('audio_data')
               # print(audio_data_base64)
               audio_data = base64.b64decode(audio_data_base64)
               audio_io = io.BytesIO(audio_data)
               data_samples=extract_features(audio_io,None)

               data_samples_normalized = scaler.transform(data_samples)
               prediction=model.predict(data_samples_normalized)
               return jsonify({'Music category': prediction[0]})

          except Exception as e:
               return jsonify({'error': str(e)})


def extract_features(audio_file,sampling_rates):
     x, sr = librosa.load(audio_file,sr=sampling_rates)
     onset_env = librosa.onset.onset_strength(y=x, sr=sr)

     tempo = librosa.feature.tempo(onset_envelope=onset_env, sr=sr)


     features = {
    "chroma_stft_mean": float(librosa.feature.chroma_stft(y=x, sr=sr).mean()),
    "chroma_stft_var": float(librosa.feature.chroma_stft(y=x, sr=sr).var()),
    "rms_mean": float(librosa.feature.rms(y=x).mean()),
    "rms_var": float(librosa.feature.rms(y=x).var()),
    "spectral_centroid_mean": float(librosa.feature.spectral_centroid(y=x, sr=sr).mean()),
    "spectral_centroid_var": float(librosa.feature.spectral_centroid(y=x, sr=sr).var()),
    "spectral_bandwidth_mean":float( librosa.feature.spectral_bandwidth(y=x, sr=sr).mean()),
    "spectral_bandwidth_var": float(librosa.feature.spectral_bandwidth(y=x, sr=sr).var()),
    "rolloff_mean": float(librosa.feature.spectral_rolloff(y=x, sr=sr).mean()),
    "rolloff_var": float(librosa.feature.spectral_rolloff(y=x, sr=sr).var()),
    "zero_crossing_rate_mean": float(librosa.feature.zero_crossing_rate(y=x).mean()),
    "zero_crossing_rate_var": float(librosa.feature.zero_crossing_rate(y=x).var()),
    "harmony_mean": float(librosa.effects.harmonic(y=x).mean()),
    "harmony_var": float(librosa.effects.harmonic(y=x).var()),
    "tempo":float(tempo[0])
     }
  # Extract the MFCC features.
     mfccs = librosa.feature.mfcc(y=x, sr=sr)
     for i in range(1, 21):
          features["mfcc{}_mean".format(i)] =float( mfccs[i - 1].mean())
          features["mfcc{}_var".format(i)] = float(mfccs[i - 1].var())

     # print("Feature Values:")
     # for value in features.values():
     #     print(value)


     return [list(features.values())]

               
if __name__ == '__main__':
          app.run(debug=True)
