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

# Import pandas
import pandas as pd

# Import pyplot module to plot the results
import matplotlib.pyplot as plt

# Import train_test_split module to split the data into train and test
from sklearn.model_selection import train_test_split

# Import LinearRegression module to use in model training
from sklearn.linear_model import LinearRegression

# Import gdown module to download files from google drive
import gdown

# Import zip file module to open the zip file
from zipfile import ZipFile

#--------------------------------------------- Get the file location from google drive  ---------------------------------------------------

# Please change the URL as needed (make sure you have the access to the file)

url = 'https://drive.google.com/file/d/1dVBMQb-eKRq92WMKfJDbTBt-j-W_5s5u/view?usp=sharing'

# Derive the file id from the URL
file_id = url.split('/')[-2]

# Derive the download url of the the file
download_url = 'https://drive.google.com/uc?id=' + file_id

# Give the location you want to save it in your local machine
file_location = 'solar.zip'

#--------------------------------------------- Download and extract the zip file -----------------------------------------------------------

# Download the file from drive to your local machine
gdown.download(download_url, file_location)

# Open the downloaded zip file and extract its contents
with ZipFile(file_location, "r") as zip_file:
    zip_file.extractall()
    
# ------------------------------------------------- Read and combine the CSVs --------------------------------------------------------------

# Read 1st csv file
plant = pd.read_csv('solar/Plant_2_Generation_Data.csv', sep = ',', engine = 'python', header = 0)

# Read 2nd csv file
weather = pd.read_csv('solar/Plant_2_Weather_Sensor_Data.csv', sep = ',', engine = 'python', header = 0)

# Combine the two csv files using DATE_TIME coloumn
combined_file = plant.merge(weather, on=["DATE_TIME", "PLANT_ID"], suffixes=("_GENERATION", "_WEATHER"))

# Save the combined as a csv
combined_file.to_csv('output.csv', sep = ',')

#------------------------------------------------- Start the training and prediction --------------------------------------------------------

# Get feature coloumns
X2 = combined_file[['AMBIENT_TEMPERATURE', 'MODULE_TEMPERATURE', 'IRRADIATION']]

# Get target coloumn
y2 = combined_file['AC_POWER']

# Split the data into train and test
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.3)

# Initialize LinearRegression class
lm2 = LinearRegression()

# Fit the training data
lm2.fit(X2_train, y2_train)

# Get the predictions
predictions = lm2.predict(X2_test)

# ----------------------------------------------- Plot the results --------------------------------------------------------------------------

plt.scatter(y2_test, predictions)
plt.title('Actual Solar Output Values vs Predicted Values for Plant 2')
plt.xlabel('Predicted Output')
plt.ylabel('Actual Output')

plt.show()