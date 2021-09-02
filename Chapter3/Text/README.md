
What it does :

    1. Read text data in python and print word by word or sentence by sentence.

Dependancies :

These dependancies are needed only for printing a text document, sentence by sentence

    1. nltk module is needed to be installed in the local machine to run this program.

    2. Download 'punkt' module using nltk
       open a python command line and run the following code
       import nltk
       nltk.download('punkt')

Why do we need 'punkt' module : 

The sent_tokenize function uses an instance of PunktSentenceTokenizer from the nltk.tokenize.punkt module, which is already well trained. So it knows to mark the end and beginning of a sentence properly.

Things to check before running :

    1. Check whether you have given the correct location of your text file.
    2. Check whether you file format is correct.
    3. Check whether you have access to the file.