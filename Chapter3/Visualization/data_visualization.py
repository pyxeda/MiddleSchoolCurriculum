# python program to visualize histograms and bar plots of data columns
    
# import modules
import pandas as pd
import matplotlib.pyplot as plt
import os

# get the current working directory
dir = os.path.dirname(__file__)

# Please change the filename as needed
filename = 'child vs adult.csv'

file_location = os.path.join(dir, filename)

try:
    # read the CSV file
    data = pd.read_csv(file_location)

    # print the details of the dataset including the column names. 
    # you can use these details when selecting the column names for the following plots.
    print ('Details of the dataset:')
    data.info()

    # get the column names of the dataset
    column_names = data.columns
    
    # ------------------------------------------------------------------------------------------------------------ #
    # ------------------------------------------- Plot the Histogram --------------------------------------------- #
    # ------------------------------------------------------------------------------------------------------------ #

    # select a column name to plot the hoistogram, after visulaising the details of the dataset.
    histogram_data = 'Child'

    # visualize the histogram of the selected column
    if  histogram_data in column_names:
        
        # get the data of the selected column
        x = data[histogram_data]

        # plot the histogram (you can change the number of bins and the color as you needed)
        plt.hist(x, bins = 30, color = 'green')

        # set the title, x-axis name and the y-axis name of the plot
        plt.title('Histogram for ' + histogram_data + 's')
        plt.xlabel('Number of ' + histogram_data + 's')
        plt.ylabel('Frequency')
        
        # show the plot
        plt.show()

    else:
        print ('Column name to plot the histogram cannot be found. Please provide a correct column name!')

    # ------------------------------------------------------------------------------------------------------------ #
    # ------------------------------------------- Plot the Bar Graph --------------------------------------------- #
    # ------------------------------------------------------------------------------------------------------------ #

    # select the column names to plot the bar graph, after visulaising the details of the dataset
    # according to the dataset you can change the number of y axis columns as you needed
    column_x_axis = 'Year of registration'
    column_y_axis_1 = 'Adult'
    column_y_axis_2 = 'Child'
    
     # visualize the bar plot of selected columns
    if column_x_axis and column_y_axis_1 and column_y_axis_2 in column_names:
        
        # create the dataframe
        df = pd.DataFrame({
        column_x_axis: data[column_x_axis],
        column_y_axis_1: data[column_y_axis_1],
        column_y_axis_2: data[column_y_axis_2]})

        # plot the bar graph
        df.plot(x=column_x_axis, y=[column_y_axis_1, column_y_axis_2], kind="bar")

        # set the title, x-axis name and the y-axis name of the plot
        plt.title('Bar graph for ' + filename)
        plt.xlabel(column_x_axis)
        plt.ylabel('Frequency')

        # show the plot
        plt.show()

    else:
        print ('Column names to plot the bar graph cannot be found. Please provide column names correctly!')

except Exception as e:
    print ('File cannot be found. Please provide the correct file name!')
    print (e)

