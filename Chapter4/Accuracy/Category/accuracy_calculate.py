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


# Python code to calculate the accuracy (3 category case), for given two lists. 
# list _1 is actual labels and list_2 is AI predictions. 


# Import accuracy_score function to calculate the accuracy 
from sklearn.metrics import accuracy_score


# --------------------------------------------- Input lists --------------------------------------------

# Change the lists; 'actual_label' and 'ai_predictions' as you needed

# Actual labels
actual_labels = ['cat', 'cat', 'racoon', 'racoon', 'dog', 'cat', 'dog', 'racoon']

# Predicted labels   
ai_predictions = ['racoon', 'cat', 'racoon', 'dog', 'dog', 'cat', 'cat', 'racoon'] 


# -------------------------------- Accuracy calculation starts here -------------------------------------

try:      
    # Claculate the accuracy
    accuracy =  accuracy_score(actual_labels, ai_predictions)   
        
    # Calculate the accuracy percentage
    accuracy_percentage = accuracy * 100

    # Print the accuracy
    print ('Accuaracy: ', accuracy)
    
    # Print the percentage of the accuracy
    print ('Accuracy Percentage: ', str(accuracy_percentage), '%')

except Exception as e:
    # Notifying the user about the error
    print (e)