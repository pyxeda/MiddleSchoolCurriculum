# Python program to read an image and display it

import cv2
import os

# get the current working directory
dir = os.path.dirname(__file__)

# Please change the filename as needed
filename = 'dog_1.jpeg'

file_location = os.path.join(dir, filename)

try:
  # Read the image
  image = cv2.imread(file_location) 

  # Output image with window name as 'Image' 
  cv2.imshow('Image', image) 

  # Maintain output window utill user presses a key 
  cv2.waitKey(0)		 

  # Destroying present windows on screen 
  cv2.destroyAllWindows() 

except:
  print ('Cannot find the file location. Please provide the right file location')