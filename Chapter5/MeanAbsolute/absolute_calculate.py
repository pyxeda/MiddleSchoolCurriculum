
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

# Python code to calculate the Mean Absolute Error (MAE), for given two lists. 
# list _1 is actuals and list_2 is AI predictions. 

# Import mean_absolute_error for sklearn based calculation
from sklearn.metrics import mean_absolute_error


# ------------------------------------ Initialize the variables ----------------------------------------

# Variable to count the no. of actual items 
count = 0

# Variable to get error sum
error_sum = 0

# ------------------------------------ Validation of inputs ---------------------------------------------

# Actuals
actuals = [12, 13, 14, 15, 15, 22, 27]

# Predictions  
predictions = [11, 13, 14, 14, 15, 16, 18]  

# ------------------------------------ MAE Calculation without sklearn -----------------------------------

# Iterate through each item of the list 'actuals'
for item in range(len(actuals)):

    # Increase the count by 1, when iterating
    count += 1

    # Calculate the difference between actual value and predicted value           
    error = actuals[item] - predictions[item]

    # Sum up the errors
    error_sum += error

# Calculate the mean absolute error
mae_without_sklearn = error_sum / count

# Print the MAE value
print ('Mean Absolute Error without sklearn : ', mae_without_sklearn)
    
# ------------------------------------ MAE Calculation with sklearn ----------------------------------------

mae_with_sklearn = mean_absolute_error(actuals, predictions)

# Print the MAE value
print ('Mean Absolute Error with sklearn : ', mae_with_sklearn)

