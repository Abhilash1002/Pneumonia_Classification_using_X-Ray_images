import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import tensorflow as tf
import cv2

def getModel():
    #from tensorflow import load_model
    modelqw = tf.keras.models.load_model('C:\\Users\\lenovo\\source\\repos\\Pneumonia_Classification\\mega_project\\imgup\\model.h5')
    #modelqw.summary()
    return modelqw
def preprocessing(img):
    training_data = []
    IMG_SIZE = 150
    img_array = cv2.imread('C:\\Users\\lenovo\\source\\repos\\Pneumonia_Classification\\mega_project\\media\\' + img ,cv2.IMREAD_COLOR)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    training_data.append([new_array])
    X = training_data[0][0]
    X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 3)
    model = getModel() 
    pred = model.predict_classes(X)
    prob = model.predict_proba(X)
    #print("OUTPUT = ", pred)
    #print("probability = ",prob)
    results = {'outcome':pred , 'probability':prob}
    return results
