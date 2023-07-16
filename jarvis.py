from brain.aibrain import replybrain
from brain.qna import qna
from body.listen import micexecute
print(">> Starting The Jarvis : Wait For Some Seconds.")
from body.speech import speak



def mainexe():
    
    speak("main execution have been started")
    speak("Hello sir!")
    speak("I'm Jarvis, I'm ready to assist you Sir. ")



    while True:
        data = micexecute()
        data=str(data)
        if "what is "in data or "where is" in data or "question" in data or "answer" in data:
            r=qna(data)
        else:
            r=replybrain(data)
        speak(r)

mainexe()

