import speech_recognition as sr
from googletrans import Translator


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
    return querry

def translationtohindi(Text):

    line =str(Text)
    translate=Translator()
    result=translate.translate(line)
    data=result.text
    print(f"You : {data}.")
    return data



def micexecute():
    querry=listen()
    data =translationtohindi(querry)
    return data

micexecute()
