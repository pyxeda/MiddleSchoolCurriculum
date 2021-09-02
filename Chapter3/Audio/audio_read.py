# Python program to read an audio file in a specific location and play it

# Import mixer to play audio
from pygame import mixer

# Import gdown module to download files from google drive
import gdown

#--------------------------------------------- Get the file location from google drive ----------------------------------------
    
# Please change the URL as needed (make sure you have the access to the file)

url = 'https://drive.google.com/file/d/14A91Km8obCo7ohpfEr4_Nel5d8uKPiAl/view?usp=sharing'

# Derive the file id from the URL
file_id = url.split('/')[-2]

# Derive the download url of the the file
download_url = 'https://drive.google.com/uc?id=' + file_id

# Give the location you want to save it in your local machine
file_location = r'children_1.mp3'

#--------------------------------------------- Download the audio file and play it --------------------------------------------

try:
    # Download the file from drive to your local machine
    gdown.download(download_url, file_location)

    # Initialize the mixer
    mixer.init()

    # Load the music file by giving the location
    mixer.music.load(file_location)

    # Start playing the audio
    mixer.music.play()

    # Infinite loop
    while True:
        print("Press 'p' and enter to pause, 'r' and enter to resume")
        print("Press 'e' and enter to exit the program")

        # Check keyboard input
        keyboard_input = input(" ")
        
        if keyboard_input == 'p':
            # Pausing the audio
            mixer.music.pause()
        elif keyboard_input == 'r':
            # Resuming the audio
            mixer.music.unpause()
        elif keyboard_input == 'e':
            # Stop the audio
            mixer.music.stop()
            break
# Catch the keyboard Intercept action
except KeyboardInterrupt:
    print('Program stopped by user.')
# Notifying the user about the error
except Exception as e:
    print('File location or format incorrect/ You do not have the access')
