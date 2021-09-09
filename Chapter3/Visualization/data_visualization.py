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


# Python program to visualize histograms and bar plots of data columns

    
# Import pandas module to read the CSV file and to process the tabular data
import pandas as pd

# Import matplotlib module for the data visualization
import matplotlib.pyplot as plt

# Import gdown module to download files from google drive
import gdown


# -------------------------- Get the file location from the google drive. ---------------------------------

# Please change the url as needed (make sure you have the access to the file)
url = 'https://drive.google.com/file/d/1J5z8OsAtgSp9i1eLxQFoxVexSZJuhI_-/view?usp=sharing'

# Derive the file id from the url
file_id = url.split('/')[-2]

# Derive the download url of the file
download_url = 'https://drive.google.com/uc?id=' + file_id

# Give the location you want to save it in your local machine
file_location = r'child vs adult.csv'


# ---- Downloading, Reading and Visualization of data from the provided file location, will start now. ----

try:
    # Download the file from drive to your local machine
    gdown.download(download_url, file_location)

    # Read the CSV file
    data = pd.read_csv(file_location)

    # Print the details of the dataset including the column names. 
    # You can use these details when selecting the column names for the following plots.
    print ('-------------- Details of the Dataset --------------')
    data.info()

    # Get the column names of the dataset
    column_names = data.columns

    
    # ------------------------------------------- Plot the Histogram --------------------------------------------- #
   
    # Select a column name to plot the hoistogram, after visulaising the details of the dataset.
    histogram_data = 'num_countries'

    # Visualize the histogram of the selected column
    if  histogram_data in column_names:
        
        # Get the data of the selected column
        x = data[histogram_data]

        # Plot the histogram (you can change the number of bins and the color as you needed)
        plt.hist(x, bins = 30, color = 'green')

        # Set the title, x-axis name and the y-axis name of the plot
        plt.title('Histogram for ' + histogram_data + 's')
        plt.xlabel('Number of ' + histogram_data + 's')
        plt.ylabel('Frequency')
        
        # Show the plot
        plt.show()

    # If you have provided a column name which cannot be seen under 'Details of the Dataset',
    else:
        print ('Column name to plot the histogram cannot be found. Please provide a correct column name!')

    
    # ------------------------------------------- Plot the Bar Graph --------------------------------------------- #

    # Select the x axis to plot the bar graph, after visulaizing the details of the dataset
    x_axis = 'num_countries'
    
    # Visualize the bar plot 
    if x_axis in column_names:
        
        # Plot the bar graph
        bargraph = data.plot.bar(x = x_axis)
        
        # Show the plot
        plt.show()

    # If you have provided a x axis name which cannot be seen under 'Details of the Dataset',
    else:
        print ('x axis name to plot the bar graph cannot be found. Please provide column names correctly!')

except Exception as e:
  # Notifying the user about the error
  print ("File location or format incorrect/ You don't have the access!")

