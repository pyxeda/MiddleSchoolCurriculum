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

# Import resnet50 pretrained model
from keras.applications.resnet import ResNet50

# Import image module
from keras.preprocessing import image

# Import preprocess_input and decode_predictions modules to evaluate the input
from keras.applications.resnet import preprocess_input, decode_predictions

# Import numpy module
import numpy as np

# Import gdown module to download files from google drive
import gdown

# Import zip file module to open the zip file
from zipfile import ZipFile

#--------------------------------------------- Get the file location from google drive  ----------------------------------------------------

# Please change the URL as needed (make sure you have the access to the file)

url = 'https://drive.google.com/file/d/1-FTayQ4HNMpWg9BSUE17-gbreaSsdtCf/view?usp=sharing'

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

#--------------------------------------------- Start the prediction operation --------------------------------------------------------------

# Use ResNet50 pretrained model with imagenet training
model = ResNet50(weights='imagenet')

def evaluate(img_fname):
    # Load the image
    img = image.load_img(img_fname, target_size=(224, 224))

    # Conver image into a Numpy array
    x = image.img_to_array(img)

    # Expand the array 
    x = np.expand_dims(x, axis=0)

    # Adequate your image to the format the model requires
    x = preprocess_input(x)

    # Get the predictions
    preds = model.predict(x)

    # Print the probability and category name for the 5 categories 
    # With highest probability: 
    print('Predicted:', decode_predictions(preds, top=5)[0])

# Give the path of the image you want to predict to the evaluate function as a input parameter
evaluate('Cats and Dogs (New)\Cats\Cat_1.jpg')