
from flask import Flask, request, jsonify,render_template
import requests
import os
import pickle
import joblib

import numpy as np
import librosa
from sklearn.preprocessing import StandardScaler

import io
import base64


app = Flask(__name__,static_url_path='/static')

@app.route('/')
def home():
     return render_template('form.html')

@app.route('/classifyy', methods=['POST'])
def classify_audio(): 
     if request.method == 'POST':
          audio_file=request.files['file']
          audio_data = audio_file.read()
          print("this is input")
          print(data_samples)
          selected_value = request.form['model_selected']
          
          if selected_value == "none" :
               return render_template('form.html')

          if selected_value == "svm" :
               svm_response = requests.post("http://svm_service:80/svm",json=data_samples)
               return jsonify(svm_response.text)  

          if selected_value == "vgg" :
               svm_response = requests.post("http://vgg19_service:80/vgg",json=data_samples)
               return jsonify(svm_response.text)  
          
@app.route('/classify', methods=['POST'])
def classify(): 
     if request.method == 'POST':
          audio_file=request.files['file']
          audio_data = audio_file.read()
          encoded_audio = base64.b64encode(audio_data).decode('utf-8')
          payload = {'audio_data': encoded_audio}

          selected_value = request.form['model_selected']
          
          if selected_value == "none" :
               return render_template('form.html')

          if selected_value == "svm" :
               svm_response = requests.post("http://svm_service:80/svm-base64",json=payload)
               return jsonify(svm_response.text)  

          if selected_value == "vgg" :
               # vgg19-base64
               svm_response = requests.post("http://vgg19_service:80/vgg19-base64",json=payload)
               return jsonify(svm_response.text)           

     #    try:
     #        audio_file = request.files['file']
     #        # Read the contents of the audio file
     #        audio_data = audio_file.read()
     #        # Encode the audio data as base64
            

     #        # Send a POST request to another Flask microservice
     #        microservice_url = 'http://other_microservice_url'
     #        payload = {'audio_data': encoded_audio}
     #        response = requests.post(microservice_url, json=payload)

     #        # Process the response from the other microservice as needed
     #        result = response.json()

     #        # Return the result as a JSON response
     #        return jsonify(result)

     #    except Exception as e:
     #        return jsonify({'error': str(e)})
        
       
if __name__ == '__main__':
          app.run(debug=True)
