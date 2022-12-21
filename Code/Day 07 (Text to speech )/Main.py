#------------------------------------|| 100 days of code ||------------------------------------#
# Day 07: Text to Speech

#importing modules
import pyttsx3


#taking input from user
Userinput = input("Enter the text you want to convert to speech: ")

#selecting
gender = (input(" 0 for male voice \n1 for female voice \n-->")) 
gender = int(gender)

# asking user if he/she wants to chage the speed of the voice
voice_rate = input("Do you want to change the speed of the voice? (y/n) ")
if voice_rate == 'y':
    raw_rate = input("S - Slow \nN - Normal \nF - Fast \nM-Mannual \n-->")
    raw_rate = raw_rate.upper()
    if raw_rate == 'S':
        rate = 100
    elif raw_rate == 'N':
        rate = 150
    elif raw_rate == 'F':
        rate = 200
    elif raw_rate == 'M':
        rate = input("Enter the speed you want: ")
        rate = int(rate)
#handling errors
#initializing the engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', rate)
try:
    engine.setProperty('voice', voices[gender].id)
except:
    print("Invalid input")
    exit()

def speak():
    engine.say(Userinput)
    engine.runAndWait()
    return engine
speak()

#asking user if he/she wants to save the audio file
save = input("Do you want to save the audio file? (y/n) ")
if save == 'y':
    engine.save_to_file(Userinput, 'audio.mp3')
    engine.runAndWait()
    print("Audio file saved as audio.mp3")
else:
    print("Audio file not saved")
    #------------------------------------|| 100 days of code ||------------------------------------#
# Day 07: Text to Speech

#importing modules
import pyttsx3


#taking input from user
Userinput = input("Enter the text you want to convert to speech: ")

#selecting
gender = (input(" 0 for male voice \n1 for female voice \n-->")) 
gender = int(gender)

# asking user if he/she wants to chage the speed of the voice
voice_rate = input("Do you want to change the speed of the voice? (y/n) ")
if voice_rate == 'y':
    raw_rate = input("S - Slow \nN - Normal \nF - Fast \nM-Mannual \n-->")
    raw_rate = raw_rate.upper()
    if raw_rate == 'S':
        rate = 100
    elif raw_rate == 'N':
        rate = 150
    elif raw_rate == 'F':
        rate = 200
    elif raw_rate == 'M':
        rate = input("Enter the speed you want: ")
        rate = int(rate)
#handling errors
#initializing the engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', rate)
try:
    engine.setProperty('voice', voices[gender].id)
except:
    print("Invalid input")
    exit()

def speak():
    engine.say(Userinput)
    engine.runAndWait()
    return engine
speak()

#asking user if he/she wants to save the audio file
save = input("Do you want to save the audio file? (y/n) ")
if save == 'y':
    engine.save_to_file(Userinput, 'audio.mp3')
    engine.runAndWait()
    print("Audio file saved as audio.mp3")
else:
    print("Audio file not saved")
    
