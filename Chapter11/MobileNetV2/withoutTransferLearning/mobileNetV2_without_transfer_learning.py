'''Copyright (c) 2021 AIClub

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
documentation files (the "Software"), to deal in the Software without restriction, including without 
limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of 
the Software, and to permit persons to whom the Software is furnished to do so, subject to the following 
conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT 
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO 
EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN 
AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE 
OR OTHER DEALINGS IN THE SOFTWARE.'''

# Python program to train cats and dogs dataset with the MobileNetV2 in tensorflow (Without transfer learning)

# Import tensorflow
import tensorflow as tf

# Import keras
from tensorflow import keras

# Import preprocess_input for ImageDataGenerator class
from keras.applications.mobilenet import preprocess_input

# Import ImageDataGenerator class for the Data Augmentation
from keras.preprocessing.image import ImageDataGenerator

# Import gdown module to download files from google drive
import gdown

# Import zip file module to open the zip file
from zipfile import ZipFile

#--------------------------------------------- Get the file location from google drive  ----------------------------------------
    
# Please change the URL as needed (make sure you have the access to the file)

url = 'https://drive.google.com/file/d/1fMHrqIY0QYEj9qFUFsDuF949Jo-UWzVX/view?usp=sharing'

# Derive the file id from the URL
file_id = url.split('/')[-2]

# Derive the download url of the the file
download_url = 'https://drive.google.com/uc?id=' + file_id

# Give the location you want to save it in your local machine
file_location = 'cats_and_dogs.zip'

#--------------------------------------------- Download and extract the zip file -----------------------------------------------------------

# Download the file from drive to your local machine
gdown.download(download_url, file_location)

# Open the downloaded zip file and extract its contents
with ZipFile(file_location, "r") as zip_file:
    filepath = zip_file.extractall()
    # Read train and test datasets
    train_path = r"test_set\test_set"
    test_path = r"training_set\training_set"

#--------------------------------------------- Begin the training operation using MobileNetV2 -----------------------------------

# Give image size and shape
IMG_SIZE = 224
IMG_SHAPE = (IMG_SIZE, IMG_SIZE, 3)

# Go through the train directory to obtain cateogries
train_batches = ImageDataGenerator(preprocessing_function=preprocess_input).flow_from_directory(
                train_path ,target_size=(IMG_SIZE,IMG_SIZE),batch_size=24,class_mode='categorical')

# Go through the test directory to obtain cateogries
test_batches = ImageDataGenerator(preprocessing_function=preprocess_input).flow_from_directory(
                test_path ,target_size=(IMG_SIZE,IMG_SIZE),batch_size=24,class_mode='categorical')

# Get the base model using MobileNetV2 without a pre trained moded(weight = None)
# Dont make trainable as false(keras trainable is true by default)
base_model = keras.applications.MobileNetV2(input_shape=IMG_SHAPE,include_top=False,weights=None)

feature_batch = base_model.output
global_average_layer = keras.layers.GlobalAveragePooling2D()
feature_batch_average = global_average_layer(feature_batch)
prediction_layer = keras.layers.Dense(2)
prediction_batch = prediction_layer(feature_batch_average)

# Group layers into a keras model
model = keras.Sequential([
  base_model,
  global_average_layer,
  prediction_layer
])

# Complile the model
model.compile(optimizer=tf.keras.optimizers.RMSprop(),
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Fit the training data
history = model.fit(train_batches,
                         steps_per_epoch=24,
                         epochs=1, #<-- increase for higher accuracy
                         validation_data=test_batches,
                         validation_steps=200)

# Get the accuracy
loss,accuracy = model.evaluate(test_batches, steps = 20)

print('Accuracy :', accuracy)