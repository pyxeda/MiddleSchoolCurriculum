# Python program to read an image and display it


# Import opencv module to read and display images
import cv2

# Import gdown module to download files from google drive
import gdown


# -------------------------- Get the file location from the google drive. ---------------------------------

# Please change the url as needed (make sure you have the access to the file)
url = 'https://drive.google.com/file/d/1CokCuNkyP1zvuTXj_-hxIwevXz4TG9SA/view?usp=sharing'

# Derive the file id from the url
file_id = url.split('/')[-2]

# Derive the download url of the file
download_url = 'https://drive.google.com/uc?id=' + file_id

# Give the location you want to save it in your local machine
file_location = r'dog.png'


# --- Downloading, Reading and Displaying of the image from the provided file location, will start now. ---

try:
  # Download the file from drive to your local machine
  gdown.download(download_url, file_location)
  
  # Read the image
  image = cv2.imread(file_location) 

  # Output image with window name as 'Image' 
  cv2.imshow('Image', image) 

  # Maintain output window utill user presses a key 
  cv2.waitKey(0)		 

  # Destroying present windows on screen 
  cv2.destroyAllWindows() 

except Exception as e:
  # Notifying the user about the error
  print ("File location or format incorrect/ You don't have the access!")