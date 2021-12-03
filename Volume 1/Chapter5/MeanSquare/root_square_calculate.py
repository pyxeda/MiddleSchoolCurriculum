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


# Python code to calculate the Root Mean Square Error(RMSE), for given two lists. 
# list _1 is actual labels and list_2 is AI predictions. 


# Import mean_squared_error function for error calculations
from sklearn.metrics import mean_squared_error 

# Import sqrt function to get the square root of the mean_squared_error
from math import sqrt


# ------------------------------------------ Input lists ------------------------------------------------

# Change the lists; 'actual_labels' and 'ai_predictions' as you needed

# Actual labels
actual_labels = [1, 2, 5, 2.3, 5, 4.6, 3.7]

# Predicted labels   
ai_predictions = [-1, 4, 3, 4.3, 7, 2.6, 5] 


# ----------------------------------- RMSE calculation without using libraries -------------------------------------

# Initialise the variable to sum up all the squared errors
squaredErrorSum = 0

# Iterate through the each index of actual labels in the list 'labels'
for label in range(len(actual_labels)):

    # Calculate the error between actual label and predicted label           
    error = actual_labels[label] - ai_predictions[label]

    # Square the error found in above step
    squareError = error**2

    # Sum up the squared errors
    squaredErrorSum += squareError

# Calculate the mean square error 
mse_without_sklearn = squaredErrorSum / len(actual_labels)

# Calculate the root mean square error 
rmse_without_sklearn = mse_without_sklearn ** 0.5

# Print the rmse value
print ('RMSE without using sklearn: ', rmse_without_sklearn)


# ------------------------------------- RMSE calculation using libraries ------------------------------------------

# Calculate the mean squared error 
mse_using_sklearn = mean_squared_error(actual_labels, ai_predictions)

# Calculate the root mean squared error 
rmse_using_sklearn = sqrt(mse_using_sklearn)

# Print the rmse value
print ('RMSE using sklearn: ', rmse_using_sklearn)



    
