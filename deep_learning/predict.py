# -*- coding=utf-8 -*-
import os
import sys
import numpy as np
import keras
from keras.models import load_model
from keras.preprocessing import image

IMG_HEIGHT = 80
IMG_WIDTH = 60
IMG_COLOR = 3

# load image
img = image.load_img(sys.argv[1], target_size=(IMG_HEIGHT, IMG_WIDTH))
imgary = image.img_to_array(img)

# load model
model = load_model('./misawa_top4.h5')

# predict
print(model.predict(np.array([imgary,])))
