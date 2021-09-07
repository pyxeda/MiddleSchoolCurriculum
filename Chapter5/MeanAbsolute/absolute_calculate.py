
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


# ------------------------------------ Initialize the variables ----------------------------------------

# Variable to count the no. of actual items 
count = 0

# Variable to get error sum
error_sum = 0

# Initialize the variable to check the validity of the given lists
lists_valid = False

# ------------------------------------ Validation of inputs ---------------------------------------------

try:   
    # Actuals
    actuals = [12, 13, 14, 15, 15, 22, 27]

    # Predictions  
    predictions = [11, 13, 14, 14, 15, 16, 18]

# Notifying the user about the error  
except Exception as e:
    print ('Please provide valid elements')
    print (e)

else:
    # Check whether both lists contain the same number of elements
    if len(actuals) != len (predictions):
        print('Both lists must be contain the same number of elements')

    # Check whether the lists are empty
    elif len(actuals) == 0:
        print('Lists should not be empty')

    # Confirm the user has given valid inputs for both lists
    else:
        # Make 'lists_valid' : True
        lists_valid = True

# ------------------------------------ MAE Calculation ---------------------------------------------------

# This part will only execute if the given inputs are valid
if lists_valid: 
    try:
        # Iterate through each item of the list 'actuals'
        for item in range(len(actuals)):

            # Increase the count by 1, when iterating
            count += 1

            # Calculate the difference between actual value and predicted value           
            error = actuals[item] - predictions[item]

            # Sum up the errors
            error_sum += error

        # Calculate the mean absolute error
        mae = error_sum / count

        # Print the MAE value
        print ('Mean Absolute Error : ', mae)
    except:
        print('All items of the lists, should be numbers')

    
