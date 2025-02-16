from __future__ import print_function
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.optimizers import Adadelta
from keras.utils import np_utils
from keras.regularizers import l2, activity_l2
import cPickle 
import numpy
import csv
import scipy.misc
import scipy
from scipy import ndimage
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
import processing
from PIL import Image
import sys
from pylab import *
import model


img_rows, img_cols = 48, 48
channel = 1
mimg_rows, img_cols = 48, 48
channel = 1
classes = ['Angry', 'Disgust', 'Fear', 'Happy','Sad','Surprise','Neutral'];

weights_path_ICML = './model/Model.1156-0.6729.hdf5'
model_ICML = model.model_ICML()
model_ICML.load_weights(weights_path_ICML)
#print("Model loaded successfully")

weights_path_VGG = './model/Model.356-0.6796.hdf5'
model_VGG = model.model_VGG_face()
model_VGG.load_weights(weights_path_VGG)
#print("Model loaded successfully")

VGG_19_weigth_path = "./model/VGG_19_Model.310-0.6668.hdf5"
model_VGG_19 = model.model_VGG_19_face()
model_VGG_19.load_weights(VGG_19_weigth_path)
#print("Model loaded successfully")

filename = sys.argv[1]
img = array((Image.open(filename).convert('L')).resize((img_rows, img_cols)),'f')
tmpdata = processing.Process(img)
inputdata = np.empty((1,channel,img_rows,img_cols),dtype="float32")
inputdata[0,0,:,:] = tmpdata

out_ICML = model_ICML.predict_proba(inputdata,batch_size=128, verbose=0)
out_VGG = model_VGG.predict_proba(inputdata,batch_size=128, verbose=0)
out_VGG_19 =model_VGG_19.predict_proba(inputdata,batch_size=128, verbose=0)

final_out = out_ICML + out_VGG + out_VGG_19

index = 0;
tmp_value = 0;
for j in range(0,7):
    if final_out[0][j] > tmp_value:
        index = j
        tmp_value = final_out[0][j]

print(index)







