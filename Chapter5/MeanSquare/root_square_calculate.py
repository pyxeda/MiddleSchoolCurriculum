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


# ------------------------------------ Initialise the variables ----------------------------------------

# Initialise the variable to count the no. of actual labels 
count = 0

# Initialise the variable to sum up all the squared errors
squaredErrorSum = 0

# Initialise the variable to check the validity of the given lists
listsValid = False


# ------------------------------- Giving inputs and validation of inputs --------------------------------

# Change the lists; 'labels' and 'aiPredictions' as you needed
try:
    # Actual labels
    labels = [1, 2, 5, 2.3, 5, 4.6, 3]

    # Predicted labels   
    aiPredictions = [-1, 4, 3, 4.3, 7, 2.6, 5] 

except Exception as e:
    # Notifying the user about the error
    print ('Please provide valid elements')
    print (e)

else:
    # Check whether both lists are contain the same number of elements
    if len(labels) != len (aiPredictions):
        # If the number of elements in the 2 lists are not same,
        print ('Both lists must be contained the same number of elements')

    # Check whether the lists are empty
    elif len(labels) == 0:
        # If the lists are empty,
        print ('Lists should not be empty')

    # Confirm the user has inputted valid lists
    else:
        # Make the variable name 'listsValid' True
        listsValid = True


# ------------------------------------ RMSE calculation starts here -----------------------------------------

# This part will only execute if the given inputs are valid
if listsValid: 

    try: 

        # Iterate through the each index of actual labels in the list 'labels'
        for label in range(len(labels)):

            # Increase the count by 1, after iterated through each actual label
            count += 1

            # Calculate the error between actual label and predicted label           
            error = labels[label] - aiPredictions[label]

            # Square the error found in above step
            squareError = error ** 2

            # Sum up the squared errors
            squaredErrorSum += squareError

        # Calculate the mean square error 
        mse = squaredErrorSum / count

        # Calculate the root mean square error 
        rmse = mse ** 0.5

        # Print the rmse value
        print ('Root Mean Square Error (RMSE): ', rmse)

    except:
        print ('All items of the lists, should be numbers')
    
