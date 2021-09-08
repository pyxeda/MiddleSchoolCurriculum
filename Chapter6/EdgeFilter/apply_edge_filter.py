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


# Python program to apply an edge filter (sobel) and visualize the filtered image..


# Import opencv module to read, resize, and display images
import cv2

# Import gdown module to download files from the google drive
import gdown

from matplotlib import pyplot as plt


# ------------------------------- Get the file location from the google drive. ---------------------------------

# Please change the url as needed (make sure you have the access to the file)
url = 'https://drive.google.com/file/d/1qWTeephmlGic3lsAefx6UstyX7WlEaUL/view?usp=sharing'

# Derive the file id from the url
file_id = url.split('/')[-2]

# Derive the download url of the file
download_url = 'https://drive.google.com/uc?id=' + file_id

# Give the location you want to save it in your local machine
file_location = r'dog.png'


# --------------------------- Downloading and Processing of the image will start now. ----------------------------

try:
    # Download the file from drive to your local machine
    gdown.download(download_url, file_location)

    # Read the original image
    original_image = cv2.imread(file_location) 

    # Convert the original image to grayscale
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

    # Apply the sobel filter to detect edges in given direction
    # If you want to detect edges only in horizontal direction, make dx=1 and dy=0
    # If you want to detect edges only in vertical direction, make dx=0 and dy=1
    # If you want to detect edges only in both directions, make dx=1 and dy=1
    # You can change the kernal size (ksize) appropriately 
    edge_filtered_image = cv2.Sobel(src=gray_image, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)  
    
    # Output the original image with window name as 'Original Image' 
    cv2.imshow('Original Image', original_image) 

    # Output the edge filtered image with window name as 'Edge Filtered Image' 
    cv2.imshow('Edge Filtered Image', edge_filtered_image) 

    # Maintain the output window util user presses a key 
    cv2.waitKey(0)		 

    # Destroying the present windows on screen 
    cv2.destroyAllWindows() 

except Exception as e:
  # Notifying the user about the error
  print ("File location or format incorrect/ You don't have the access!")  