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

# Read text data (like log files) in python and print line by line

#------------------------------------------------ Read Text line by line ------------------------------------------------------------

# Import gdown module to download files from google drive
import gdown

#------------------------------------------------ Get the file location from Google Drive -------------------------------------------
    
# Please change the URL as needed

url = 'https://drive.google.com/file/d/1ydfmj1HosSIUtT7LnJL05cfLsItgMqqo/view?usp=sharing'

# Derive the file id from the URL
file_id = url.split('/')[-2]

# Derive the download url of the the file
download_url = 'https://drive.google.com/uc?id=' + file_id

# Give the location you want to save it in your local machine
file_location = r'about_us.txt'


#------------------------------------------------ Download the text file and print it -----------------------------------------------

# Download the file from drive to your local machine
gdown.download(download_url, file_location)

# Open the file in the specified location
with open(file_location) as file:

    # Read the file
    lines = file.readlines()
    
    # Initialize line count
    line_count = 0

    # Print each line of the text
    for line in lines:
        line_count += 1
        print(f'line {line_count}: {line}')


#------------------------------------------------- Read Text word by word ----------------------------------------------------------

# try:
#     # Download the file from drive to your local machine
#     gdown.download(download_url, file_location)

#     # Open the file in the specified location
#     with open(file_location) as file:

#         # Keep a word count, to check all the words are printed
#         word_count = 0

#         # Iterate through each line of the file
#         for line in file:

#             # Iterate through each word of a line after splitting
#             for word in line.split():

#                 # Add word count for every printed word.
#                 word_count = word_count + 1
#                 print('word : ', word_count)
#                 print(word)
# # Notifying the user about the error
# except:
#     print('File location or format incorrect/ You do not have the access')

