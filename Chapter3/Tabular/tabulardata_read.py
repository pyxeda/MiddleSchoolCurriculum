# Python program to read and display tabular data from a csv file


# Import pandas module to read the CSV file
import pandas as pd


# ------------------------ Get the file location from the google drive. -----------------------------

# Please change the url as needed (make sure you have the access to the file)
url = 'https://drive.google.com/file/d/1aKqueRc7yqB0ugTU6VrjG0oGnddq37bM/view?usp=sharing'

# Derive the file id from the url
file_id = url.split('/')[-2]

# Derive the download url of the file
file_location = 'https://drive.google.com/uc?id=' + file_id


# --------- Reading and Displaying of data from the provided file location, will start now. ---------

try:
    # Read the CSV file
    data = pd.read_csv(file_location)

    # Print a sample (first row) from the tabular data
    print('---------- A Sample (first row) from the Dataset ----------')
    print(data.head(1))
    
    # See the column names in the table
    column_names = data.columns
    print('---------- Column Names in the Table ----------')
    for column in column_names:
        print (column)

    # You can change the column name as you needed, after visulaising the column names
    column_name = 'Child'
    
    # Print specific column data from the tabular data
    print('---------- Data from the Column ----------')
    if column_name in column_names:
        column = data[[column_name]]
        print (column)
        
    # If you have provided a column name which cannot be seen under 'Column names in the table : ',
    else:
        print ('Column name cannot be found. Please provide a correct column name')

except Exception as e:
    # File location or format incorrect/ You don't have the access
    print ('File cannot be found. Please provide the correct file location')
    print (e)

