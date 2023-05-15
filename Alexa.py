#First part: Alexa will listen to me 
#Second Part: Alexa will speak

import speech_recognition as sr                 #Alexa understand to we
import pyttsx3                                  # python text to speech
import pywhatkit
import datetime




listener = sr.Recognizer()                      # understand our voice
engine =  pyttsx3.init('sapi5')                      #speech to us  and intilization of this engine
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)


def talk (text):
    engine.say (text)
    engine.runAndWait()




"""engine.say("I am your alexa") 
engine.say("What can i do for you")     
engine.runAndWait()"""




def take_command():
    try:
        with sr.Microphone() as  source:
            print("listening......")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            if 'Alexa' in command:
                print(command)
    except:
        pass
    return command
def run_alexa():
    command = take_command() #taking command from user     
    print(command)
    if 'play' in command:

        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime("%H:%M")
        print(time)
        talk('Current time is' + time)


             

            
run_alexa()        