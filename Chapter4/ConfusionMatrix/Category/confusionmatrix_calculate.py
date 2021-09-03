# Python program to calucalte the confusion matrix for three categories
# Multi classification

# Import pandas to calculate confusion matrix
import pandas as pd

#--------------------------------------------- Lists --------------------------------------------------------------------

# Actuals
actuals = ['a','a','b','b','b','b','b','c','c']

# Predictions
predictions = ['a','a','a','b','b','b','c','c','c']

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