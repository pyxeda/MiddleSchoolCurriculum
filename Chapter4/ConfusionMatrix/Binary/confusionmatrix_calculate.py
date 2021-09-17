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

# Python program to calucalte the confusion matrix for binary case
# Binary classification

# Import confusion_matrix for sklearn based calculation
from sklearn.metrics import confusion_matrix

# Import pandas for pandas based calculation
import pandas as pd

#--------------------------------------------- Lists --------------------------------------------------------------------

# Actuals
actuals = ['cat', 'cat', 'dog', 'cat', 'dog']

# Predictions
predictions = ['cat', 'dog', 'dog', 'cat', 'cat'] 

#--------------------------------------------- Confusion Matrix using sklearn --------------------------------------------

# Construct Confusion Matrix
constructed_confusion_matrix = confusion_matrix(predictions, actuals)
 
# Print Confusion Matrix
print("Confusion matrix using sklearn \n \n", constructed_confusion_matrix)

#--------------------------------------------- Confusion Matrix using pandas ---------------------------------------------

# Convert actual list to a series
actuals = pd.Series(actuals, name='Actual')

# Convert prediction list to a series
predictions = pd.Series(predictions, name='Predictions')

# Create Confusion Matrix
confusion_matrix = pd.crosstab(predictions, actuals)

# Print Confusion Matrix
print("\n Confusion matrix using pandas \n \n", confusion_matrix)
    
