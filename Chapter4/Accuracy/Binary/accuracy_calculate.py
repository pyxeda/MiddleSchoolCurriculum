
# Python code to calculate the accuracy (binary case), for given two lists. 
# list _1 is actual labels and list_2 is AI predictions. 


# ------------------------------------ Initialise the variables ----------------------------------------

# Initialise the variable to count the no. of actual labels 
count = 0

# Initialise the variable to count the no. of correctly predicted labels
correctPredictions = 0

# Initialise the variable to check the validity of the inputs
inputsValid = False


# ------------------------------- Giving inputs and validation of inputs --------------------------------

# Change the lists; 'label' and 'aiPredictions' as you needed
try:
    # Actual labels
    labels = ['cat', 'cat', 'dog', 'cat', 'dog']

    # Predicted labels   
    aiPredictions = ['cat', 'dog', 'dog', 'cat', 'cat'] 

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


# -------------------------------- Accuracy calculation starts here -------------------------------------

# This part will only execute if the given inputs are valid
if inputsValid: 
    # Iterate through the each index of actual labels in the list 'labels'
    for label in range(len(labels)):
        
        # Increase the count by 1, after iterated through each actual label
        count += 1
        
        # Check whether the predicted label is same as the actual label           
        if labels[label] == aiPredictions[label]:
            
            # If predicted label is same as the actual label, increase the correctPredictions by 1
            correctPredictions += 1
        
    # Calculate the accuracy 
    accuracy = correctPredictions / count
    
    # Calculate the caauracy percentage
    accuracy_percentage = accuracy * 100

    # Print the accuracy
    print ('Accuaracy: ', accuracy)
    
    # Print the percentage of the accuracy
    print ('Accuracy Percentage: ' + str(accuracy_percentage) + ' %')