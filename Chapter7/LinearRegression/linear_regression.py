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

# Python program to create a linear regression model (using scikit learn) on the 'average' dataset. 
# Calculate the accuracy.

# Import pandas to read csv
import pandas as pd

# Import train_test_split to split data as test and train
from sklearn.model_selection import train_test_split

# Import LinearRegression class to get linear regression object
from sklearn.linear_model import LinearRegression

# Import r2_score function to calculate accuracy
from sklearn.metrics import r2_score

# Import gdown module to download files from the google drive
import gdown


# ------------------------------- Get the file from the google drive. ---------------------------------

# Please use the same dataset
url = 'https://drive.google.com/file/d/1Hxksp6KSjoex0wdER032QypLUYmdLNeg/view?usp=sharing'

# Derive the file id from the url
file_id = url.split('/')[-2]

# Derive the download url of the file
download_url = 'https://drive.google.com/uc?id=' + file_id

# Give the location you want to save it in your local machine
file_location = 'average.csv'

# Download the file from drive to your local machine
gdown.download(download_url, file_location)


# ------------------------------- Create the linear regression model --------------------------------------------

# Read the CSV
average_dataset = pd.read_csv(file_location)

# Get independent variable columns
X = average_dataset[['A', 'B', 'C', 'D']]

# Get dependent variable columns
y = average_dataset['AVERAGE']

# Split dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Use LinearRegression class provided by sklearn
regressor = LinearRegression()

# Train the model
regressor.fit(X_train, y_train)

# Predict using test values
y_pred = regressor.predict(X_test)

# Get actual values and predicted values into a table
predicted_results = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(predicted_results)


# ------------------------------- Calculate the accuracy ---------------------------------------------------------

# Calculate accuracy using 'r2_score'
accuracy = r2_score(y_test, y_pred)
print('Accuracy of your model :',accuracy)






