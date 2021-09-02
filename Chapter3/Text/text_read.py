# Read text data (like log files) in python and print word by word or sentence by sentence

#------------------------------------------------ Read Text sentence by sentence ----------------------------------------------------

# Import nltk module for sentence identifying
import nltk

# Import gdown module to download files from google drive
import gdown

#------------------------------------------------ Get the file location from Google Drive -------------------------------------------
    
# Please change the URL as needed

url = 'https://drive.google.com/file/d/1UiYaAwE0aJlkgM6qplwYLRxuRbndf6vF/view?usp=sharing'

# Derive the file id from the URL
file_id = url.split('/')[-2]

# Derive the download url of the the file
download_url = 'https://drive.google.com/uc?id=' + file_id

# Give the location you want to save it in your local machine
file_location = r'about_us.txt'


#------------------------------------------------ Download the text file and print it -----------------------------------------------

try:
    # Download the file from drive to your local machine
    gdown.download(download_url, file_location)
    
    # Open the file in the specified location
    with(open(file_location) as file):

        # Read the file
        text = file.read()

        # Use sent_tokenize function to identify each sentance separately
        senetences = nltk.sent_tokenize(text)

        # Print each sentence
        for senetence in senetences:
            print(senetence)
# Notifying the user about the error
except Exception as e:
    print(e)
    print('File location or format incorrect/ You do not have the access')


#------------------------------------------------- Read Text word by word ----------------------------------------------------------

# try:
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

