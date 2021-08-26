# Python program to read an audio file in a specific location and play it

# Import mixer from pygame module
from pygame import mixer

try:
    # Initialize the mixer
    mixer.init()

    # Load the music file by giving the location
    mixer.music.load(r'children_1.mp3')

    # Start playing the audio
    mixer.music.play()

    # infinite loop
    while True:
        print("Press 'p' and enter to pause, 'r' and enter to resume")
        print("Press 'e' and enter to exit the program")
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
# Catch the keyboard Intercept action separately
except KeyboardInterrupt:
    print('Program killed by user.')
# Ask the user to input correct location, if file location is incorrect
except:
    print('Can not find the audio file. Please provide the correct location!')
