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

# Random forest for human activity prediction using UCI HAR Dataset.

# Import pandas
import pandas as pd

# Import RandomForestClassifier since we are using random forest for this problem
from sklearn.ensemble import RandomForestClassifier

# Import GridSearchCV
from sklearn.model_selection import GridSearchCV

# Import accuracy_score to calculate accuracy
from sklearn.metrics import accuracy_score

# Import gdown module to download files from google drive
import gdown

# Import zip file module to open the zip file
from zipfile import ZipFile

#--------------------------------------------- Get the file location from google drive  ----------------------------------------

# Please change the URL as needed (make sure you have the access to the file)

url = 'https://drive.google.com/file/d/1z_zn7vv-Sk60fdoQuPN3h9wkyP8H-FQR/view?usp=sharing'

# Derive the file id from the URL
file_id = url.split('/')[-2]

# Derive the download url of the the file
download_url = 'https://drive.google.com/uc?id=' + file_id

# Give the location you want to save it in your local machine
file_location = 'UCI_HAR_Dataset.zip'

#--------------------------------------------- Download and extract the zip file -------------------------------------------------

# Download the file from drive to your local machine
gdown.download(download_url, file_location)

# Open the downloaded zip file and extract its contents
with ZipFile(file_location, "r") as zip_file:
    zip_file.extractall()

#--------------------------------------------- Begin Activity prediction operation -----------------------------------------------

# Read train and test file using pandas
xtrain=pd.read_table(r'UCI HAR Dataset\train\X_train.txt',delim_whitespace=True,header=None)


xtest=pd.read_table(r'UCI HAR Dataset\test\X_test.txt',delim_whitespace=True,header=None)


ytrain=pd.read_table(r'UCI HAR Dataset\train\y_train.txt',header=None)


ytest=pd.read_table(r'UCI HAR Dataset\test\y_test.txt',header=None)

# Return first 5 raws of the xtrain dataframe
xtrain.head()

# Initialize randomforest classifier
classifier = RandomForestClassifier()

# Define parameters for GridSearchCV method below
parameters = {'n_estimators': [10, 100, 1000], 'max_depth': [3, 6, 9], 'max_features' : ['auto', 'log2']}

# Derive the model
model=GridSearchCV(classifier,parameters,n_jobs=-1,cv=4,scoring='accuracy',verbose=4)

# Fit training data
model.fit(xtrain.to_numpy(),ytrain.to_numpy().ravel().T)

# Get the predictions
ypred=model.predict(xtest)

# Calculate the accuracy of the model
accuracy=accuracy_score(ytest,ypred)

# Print accuracy score
print('Accuracy Score: '+ str(accuracy*100) + ' %')


