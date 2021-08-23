# Python program to read an image and display it

# Import OpenCV(cv2) module 
import cv2

# Please change the file location as needed
file_location = 'E:\MiddleSchoolCurriculum\Chapter3\Image\dog_1.jpeg'

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

