# Python program to calucalte the confusion matrix for binary classification

# Import pandas to calculate confusion matrix
import pandas as pd

#--------------------------------------------- Lists --------------------------------------------------------------------

# Actuals
actuals = [1, 1, 1, 1, 1, 0, 0, 1, 1, 1]

# Predictiions
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
        print ('Both lists must be contained the same number of elements')
# Notifying the user about the error
except Exception as e:
    print('Please provide items with same type in the lists!')