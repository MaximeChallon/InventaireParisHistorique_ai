import numpy as np
import keras
from keras import backend as K
from keras.layers.core import Dense, Activation
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.models import Model
from keras.applications import imagenet_utils
from sklearn.metrics import confusion_matrix
import itertools
import matplotlib.pyplot as plt
from PIL import Image
#%matplotlib inline

print("set mobile")
mobile = keras.applications.mobilenet.MobileNet()

def prepare_image(file):
    img = image.load_img(file, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return keras.applications.mobilenet.preprocess_input(img_array_expanded_dims)
    
print("taille")
url = '/home/maxime/dev/InventaireParisHistorique_ai/LUCARNE/darknet/data/images/FRANCOIS-MIRON_RUE_44-48_2015-04000-0004930.jpg'
image_size = Image.open(url)
width = image_size.width
height = image_size.height
print("width:" + str(width))
print("height:" + str(height))

print("prepare")
preprocessed_image = prepare_image(url)
print("predict")
predictions = mobile.predict(preprocessed_image)
results = imagenet_utils.decode_predictions(predictions)
results
