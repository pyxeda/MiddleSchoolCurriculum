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
actual_labels = [1, 2, 5, 2.3, 5, 4.6, 3]

# Predicted labels   
ai_predictions = [-1, 4, 3, 4.3, 7, 2.6, 5] 


# ------------------------------------ RMSE calculation starts here -----------------------------------------

try:
    # Calculate the mean squared error 
    mse = mean_squared_error(actual_labels, ai_predictions)

    # Calculate the root mean squared error 
    rmse = sqrt(mse)

    # Print the rmse value
    print ('Root Mean Squared Error (RMSE): ', rmse)

except Exception as e:
    # Notifying the user about the error
    print (e)


    
