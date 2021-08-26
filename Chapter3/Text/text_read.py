# Read text data (like log files) in python and print word by word or sentence by sentence

# The execution of this code will print a text document, sentence by sentence.

# Import nltk module
import nltk

try:
    # Open the file in the specified location
    with(open(r'about_us.txt') as file):
        # Read the file
        text = file.read()
        # Use sent_tokenize function in nltk to identify each sentance separately in your text file
        senetences = nltk.sent_tokenize(text)
        # Print each sentence in the list
        for senetence in senetences:
            print(senetence)
# Ask the user to input the correct location, if the location is incorrect
except Exception as e:
    print('Can not find the file location. Please provide the correct file location!')
    print(e)


# The execution of the below code will print a text document, word by word. You can uncomment the below code and comment out the above code if you want to run this.

# try:
#     # open file by giving the correct file location.
#     with open(r'about_us.txt') as file:
#         # We keep a word count, just to check all the words are printed
#         word_count = 0
#         # Iterate through each line of the file
#         for line in file:
#             # Iterate through each word of a line after splitting the line into a list
#             for word in line.split():
#                 # Add word count for every printed word.
#                 word_count = word_count + 1
#                 print('word : ', word_count)
#                 print(word)
# # Ask the user to provide the correct file location, if the location is incorrect
# except:
#     print('Can not find the file location. Please provide the correct file location!')

