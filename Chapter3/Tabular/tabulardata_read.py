# python program to read and display tabular data
# import modules
import pandas as pd
import os
# get the current working directory
dir = os.path.dirname(__file__)
# Please change the filename as needed
filename = 'iris_dataset.csv'
file_location = os.path.join(dir, filename)
try:
    # read the CSV file
    data = pd.read_csv(file_location)
    # print a sample (first row) from the tabular data
    print(data.head(1))
    
    # see the column names in the table
    column_names = data.columns
    for column in column_names:
        print (column)
    # provide the specific column name that you want to display
    column_name = 'petal_length'
    
    # print specific column data from the tabular data
    if column_name in column_names:
        column = data[[column_name]]
        print (column)
    else:
        print ('Column name cannot be found. Please provide a correct column name')
except:
    print ('File cannot be found. Please provide the correct location')

