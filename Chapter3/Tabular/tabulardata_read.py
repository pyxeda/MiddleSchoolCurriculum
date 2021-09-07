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


# Python program to read and display tabular data from a csv file


# Import pandas module to read the CSV file
import pandas as pd

# Import gdown module to download files from google drive
import gdown


# -------------------------- Get the file location from the google drive. ---------------------------------

# Please change the url as needed (make sure you have the access to the file)
url = 'https://drive.google.com/file/d/14M8iBxSoAoUQqt4SGtv427jrKSThIlGM/view?usp=sharing'

# Derive the file id from the url
file_id = url.split('/')[-2]

# Derive the download url of the file
download_url = 'https://drive.google.com/uc?id=' + file_id

# Give the location you want to save it in your local machine
file_location = r'child vs adult.csv'


# ----- Downloading, Reading and Displaying of data from the provided file location, will start now. ------

try:
    # Download the file from drive to your local machine
    gdown.download(download_url, file_location)

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
  # Notifying the user about the error
  print ("File location or format incorrect/ You don't have the access!")

