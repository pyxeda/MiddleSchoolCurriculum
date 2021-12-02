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

# Import Resnet50 model
from keras.applications.resnet import ResNet50

# Import ImageDataGenerator to generate train and test batches
from keras.preprocessing.image import ImageDataGenerator 

# Import Model to create the final model
from keras.models import Model

# Import keras layers
from keras.layers import Dense,GlobalAveragePooling2D

# Import adam optimizer
from tensorflow.keras.optimizers import Adam

# Import preprocess_input for ImageDataGenerator class
from keras.applications.resnet_v2 import preprocess_input

# Import gdown module to download files from google drive
import gdown

# Import zip file module to open the zip file
from zipfile import ZipFile

#--------------------------------------------- Get the file location from google drive  ----------------------------------------------------

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

#--------------------------------------------- Begin the training operation using Resnet ----------------------------------------------

# Give image size and shape
IMG_SIZE = 224
IMG_SHAPE = (IMG_SIZE, IMG_SIZE, 3)

# Define the number of classes
num_classes = 2

# Go through the train directory to obtain cateogries
train_batches = ImageDataGenerator(preprocessing_function=preprocess_input).flow_from_directory(
                train_path ,target_size=(IMG_SIZE,IMG_SIZE),batch_size=24,class_mode='categorical')

# Go through the test directory to obtain cateogries
test_batches = ImageDataGenerator(preprocessing_function=preprocess_input).flow_from_directory(
                test_path ,target_size=(IMG_SIZE,IMG_SIZE),batch_size=24,class_mode='categorical')

# Derive the resnet pretrained model without weights
base_model = ResNet50(weights= None, include_top=False, input_shape=IMG_SHAPE)

# Get the last layer and add a few extra layers to it
x = base_model.output
x = GlobalAveragePooling2D()(x)

# Add a layer with softmax activation
predictions = Dense(num_classes, activation= 'softmax')(x)

# Get the final model
model = Model(inputs = base_model.input, outputs = predictions)

# Define the base learning rate
base_learning_rate = 0.0001

# Use Adam optimizer as the optimizer of the model
adam = Adam(lr=base_learning_rate)

# Loss function IS categorical cross entropy
# Accuracy is the evaluation metric
# Compile the model
model.compile(optimizer= adam, loss='categorical_crossentropy', metrics=['accuracy'])

# Fit the training data
model.fit(train_batches, steps_per_epoch=2, epochs=2, validation_data=test_batches)

# Evaluate the model
preds = model.evaluate(test_batches, steps = 20)

# Print the accuracy
print ("Accuracy = " + str(preds[1]))