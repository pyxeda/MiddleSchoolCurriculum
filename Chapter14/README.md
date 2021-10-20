This folder include all the python code examples related to Chapter 14

activityPrediction     ->  Random Forest for activity prediction on this dataset: https://archive.ics.uci.edu/ml/datasets/human+activity+recognition+using+smartphones 
    
dataGeneration         ->  Script to generate data from this dataset: https://www.kaggle.com/anikannal/solar-power-generation-data
It has two files (a) Plant_1_Generation_Data.csv and (b) Plant_1_Weather_Sensor_Data.csv
The script do the following
    (a) For a given id, combine the above two tables, where each row belong to a unique timestamp, which is common across the two tables
    (b) Another script that can use the above to predict the solar power generation at any point.
