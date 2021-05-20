import os
from flask import Flask, render_template, request , Response    
from flask import send_from_directory
from keras.models import load_model
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from keras import backend as K
import jsonpickle
import cv2
import datetime


import numpy as np
import tensorflow as tf

app = Flask(__name__)

dir_path = os.path.dirname(os.path.realpath(__file__))
# UPLOAD_FOLDER = dir_path + '/uploads'
# STATIC_FOLDER = dir_path + '/static'
UPLOAD_FOLDER = '/tmp'
MODEL_FOLDER = 'static/model'


# load an image and predict the class
def predict(filename):
    # load the image
    img = load_img(filename, target_size=(224, 224))
    # convert to array
    img = img_to_array(img)
    # reshape into a single sample with 3 channels
    img = img.reshape(1, 224, 224, 3)
    # center pixel data
    img = img.astype('float32')
    img = img - [123.68, 116.779, 103.939]
    # load model
    model = load_model(MODEL_FOLDER + '/cats_vs_dogs_model.h5')
    # predict the class
    result = model.predict(img)
    result = result.flatten()
    result = round(result[0])
    K.clear_session()
    return result



# route http posts to this method
@app.route('/api/cvd', methods=['POST'])
def cvd():
    basename = "image"
    suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    filename = "_".join([basename, suffix])
    filename = filename + ".jpg"
    r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img_nd = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # do some fancy processing here....
    # result = predict(img_nd)
    print(img_nd)
    status = cv2.imwrite(filename,img_nd)
    result = predict(filename)
    print(result)
    if result == 0:
        response = {'message': "cat" 
                }
    else:
        response = {'message': "dog" 
                }    
    # build a response dict to send back to client
    # response = {'message': result 
    #             }
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")


if __name__ == '__main__':
    debug = True
    app.run(debug=True)
    debug = True
