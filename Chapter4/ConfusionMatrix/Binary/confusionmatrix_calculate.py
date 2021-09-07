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

# Import pandas to calculate confusion matrix
import pandas as pd

#--------------------------------------------- Lists --------------------------------------------------------------------

# Actuals
actuals = [1, 1, 1, 1, 1, 0, 0, 1, 1, 1]

# Predictions
predictions = [1, 0, 1, 0, 1, 0, 1, 1, 1, 1]

#--------------------------------------------- Calculate the Confusion Matrix --------------------------------------------

try:
    # Check whether both lists contain the same number of elements
    if len(actuals) == len (predictions):
        
        # Convert actual list to a series
        actuals = pd.Series(actuals, name='Actual')
        
        # Convert prediction list to a series
        predictions = pd.Series(predictions, name='Predictions')
        
        # Create Confusion Matrix
        confusion_matrix = pd.crosstab(predictions, actuals)

        # Print Confusion Matrix
        print("Confusion matrix \n \n", confusion_matrix)
    else:
        print ('Both lists must contain the same number of elements')
# Notifying the user about the error
except Exception as e:
    print('All items of the lists, should be of same type')