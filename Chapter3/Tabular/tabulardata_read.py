# python program to read and display tabular data

# import modules
import pandas as pd
import os

# get the current working directory
dir = os.path.dirname(__file__)

# Please change the filename as needed
filename = 'child vs adult.csv'

file_location = os.path.join(dir, filename)

try:
    # read the CSV file
    data = pd.read_csv(file_location)

    # print a sample (first row) from the tabular data
    print('Sample (first row) from the dataset : ')
    print(data.head(1))
    
    # see the column names in the table
    column_names = data.columns
    print('Column names in the table : ')
    for column in column_names:
        print (column)

    # you can change the column name as you needed, after visulaising the column names
    column_name = 'Child'
    
    # print specific column data from the tabular data
    print('Data from the column ' + column_name + ' : ')
    if column_name in column_names:
        column = data[[column_name]]
        print (column)
        
    # if you have provided a column name which cannot be seen under 'Column names in the table : ',
    else:
        print ('Column name cannot be found. Please provide a correct column name')

except Exception as e:
    print ('File cannot be found. Please provide the correct file name!')
    print (e)

