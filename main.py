import speech_recognition as sr
import os
from jarvis import mainexe


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 3
        audio = r.listen(source,0,8)

    
    try:
        print("Recognising")
        querry=r.recognize_google(audio,language='en')
    except:
        return ""
    querry=str(querry).lower()
    print(querry)
    return querry

def wakeupdetected():
    querry=listen().lower()
    if "wake up" in querry:
        print("wake up detected")
        mainexe()
    else:
        pass
while True:
    wakeupdetected()
