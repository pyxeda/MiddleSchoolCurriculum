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


# Python program to resize a color image to a fixed length and width and visualize it.


# Import opencv module to read, resize, and display images
import cv2

# Import gdown module to download files from the google drive
import gdown


# ------------------------------- Get the file location from the google drive. ---------------------------------

# Please change the url as needed (make sure you have the access to the file)
url = 'https://drive.google.com/file/d/1qWTeephmlGic3lsAefx6UstyX7WlEaUL/view?usp=sharing'

# Derive the file id from the url
file_id = url.split('/')[-2]

# Derive the download url of the file
download_url = 'https://drive.google.com/uc?id=' + file_id

# Give the location you want to save it in your local machine
file_location = r'dog.png'


# -------------------------------------- Dimensions to resize the image. ---------------------------------------

# Change the dimensions as you needed, to resize the image

# Length to resize the image
length = 224 

# Width to resize the image
width = 224      


# --------------------------- Downloading and Processing of the image will start now. ----------------------------

try:
    # Download the file from drive to your local machine
    gdown.download(download_url, file_location)

    # Read the original image
    original_image = cv2.imread(file_location) 

    # Resize the original image to the given size 
    resized_image = cv2.resize(original_image, (length, width))

    # Output the original image with window name as 'Original Image' 
    cv2.imshow('Original Image', original_image) 

    # Output the resized image with window name as 'Resized Image' 
    cv2.imshow('Resized Image', resized_image) 

    # Maintain the output window util user presses a key 
    cv2.waitKey(0)		 

    # Destroying the present windows on screen 
    cv2.destroyAllWindows() 

except Exception as e:
    # Read the error string
    error_string = str(e)

    # If user has provide invalid inputs as the length and width to resize the image,
    if 'has a wrong type' in error_string:
        # Notifying the user about the error
        print ('Plese provide valid numbers as the dimensions')
    
    else:
        # Notifying the user about the error
        print ("File location or format incorrect/ You don't have the access!")
 