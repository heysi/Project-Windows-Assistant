import datetime
import os
import time
import pyttsx3  #pip install pyttsx3==2.71
import speech_recognition as sr


#setting text to speech engine and voice rate property
engine = pyttsx3.init("sapi5")
engine.setProperty('rate', 150)


#function for synthesizer
def say(text):
    print("Assistant: " + text)
    engine.say(text)
    engine.runAndWait()


#getting input from microphone
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        query = ""
    try:
        query = r.recognize_google(audio, language='en')
        print("User: " + query)
    except sr.UnknownValueError:
        print("Sorry, I did not get that.")
    return query.lower()

#function for greeting the user once the program starts
def greet():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        say("good morning")
    elif 12 <= hour < 18:
        say("good afternoon")
    else:
        say("good evening")


#function for controlling laptop's brightness, monitor, volume.
def nircmd(said):
    if 'increase volume' in said or 'volume up' in said:
        os.system("C:/nircmd.exe changesysvolume 5000")
        say("volume increased")

    if 'decrease volume' in said or 'volume down' in said:
        os.system("C:/nircmd.exe changesysvolume -5000")
        say("volume decreased")

    if 'max volume' in said:
        os.system("C:/nircmd.exe setsysvolume 65535")
        say("max volume") 

    if 'mute' in said:
        os.system("C:/nircmd.exe mutesysvolume 1")

    if 'unmute' in said:
        os.system("C:/nircmd.exe mutesysvolume 0")
        say("volume unmuted")

    if 'stand by' in said:
        os.system("C:/nircmd.exe standby")
       

#main function that contains the commands of other functions
def main():
    nircmd(said)

if __name__ == "__main__":
    greet()
    
    while True:
        print("Assistant: Listening...")
        said = get_audio()
        main()
        
        if "write mode" in said:
            say("write mode activated.")
            while True:
                data = input(">> ")
                said = data.lower()
                if data == "deactivate":
                    break
                else:
                    main()