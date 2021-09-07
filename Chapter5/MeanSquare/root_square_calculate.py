# Python code to calculate the Root Mean Square Error(RMSE), for given two lists. 
# list _1 is actual labels and list_2 is AI predictions. 


# ------------------------------------ Initialise the variables ----------------------------------------

# Initialise the variable to count the no. of actual labels 
count = 0

# Initialise the variable to sum up all the squared errors
squaredErrorSum = 0

# Initialise the variable to check the validity of the inputs
inputsValid = False


# ------------------------------- Giving inputs and validation of inputs --------------------------------

# Change the lists; 'label' and 'aiPredictions' as you needed
try:
    # Actual labels
    labels = [1, 2, 5, 2.3, 5, 4.6, 7]

    # Predicted labels   
    aiPredictions = [0.5, 4.3, 2.1, 2.9, 8.6, 2.6, 4.5] 

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

    # Confirm the user has given valid inputs for both lists
    else:
        # Make the variable name 'inputsValid' True
        inputsValid = True


# ------------------------------------ RMSE calculation starts here -----------------------------------------

# This part will only execute if the given inputs are valid
if inputsValid: 

    # Iterate through the each index of actual labels in the list 'labels'
    for label in range(len(labels)):

        # Increase the count by 1, after iterated through each actual label
        count += 1

        # Calculate the error between actual label and predicted label           
        error = labels[label] - aiPredictions[label]

        # Square the error found in above step
        squareError = error**2

        # Sum up the squared errors
        squaredErrorSum += squareError

    # Calculate the mean square error 
    mse = squaredErrorSum / count

    # Calculate the root mean square error 
    rmse = mse**0.5

    # Print the rmse value
    print ('RMSE: ', rmse)

    
