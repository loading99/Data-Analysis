#!flask/bin/python
#Webservice related
from flask import Flask, jsonify,render_template,request
import os

#tensorflow and keras
from PIL import Image
import numpy as np
import scipy
import keras
from keras.models import load_model
from keras.utils import CustomObjectScope
from keras.initializers import glorot_uniform
from datetime import date
#Support file
import database

app = Flask(__name__)
UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello_world():
    return render_template('index.html')

#file uploaded needs to be 28x28
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image'] #file is the image uploaded
    f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    im_matrix=convert(file)
    print(im_matrix.shape)

    #Make prediction
    prediction=predict(im_matrix)
    print(prediction)
    
    #Save record to Cassandra
    database.createKeySpace(file.filename,prediction)
    file.save(f)
    return render_template('output.html',value=prediction,date=date.today().isoformat())

#convert image to digit
def convert(image_file):
    img=Image.open(image_file)
    return np.invert(img.convert('L'))

#make prediction, m is pixel matrix
def predict(m):
    mi=np.array([m])
    #Retrieve models
    with CustomObjectScope({'GlorotUniform': glorot_uniform()}):
        clf=load_model('image_model.h5')
    for i in range(10):
	    if clf.predict(mi)[0][i]==1:
	        return i
	
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)

