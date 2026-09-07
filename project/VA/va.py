import playsound
import time #shows time
import webbrowser #open to chrome
import os  #control the flow of system
import uuid #make changes in data(code)
import re  #pattern matching
from gtts import gTTS
import speech_recognition as sr
'''
text = "Welcome to Codegnan DA-23 batch"

# Convert text to speech
tts = gTTS(text)

#print(tts)
tts.save("audio.mp3")
playsound.playsound("audio.mp3")
'''
#we will use SpeechRecognition
#we will create a listen function to listen our voice
def listen():
    """Function to listen the voice"""
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("you can speak!!!")
        audio = r.listen(source,phrase_time_limit=10)
    data="" #this will be your statement
    #Exception handling
    try:
        data=r.recognize_google(audio,language='en-US')
        print("you said:"+data)
    except sr.UnknownValueError:
        print("I cannot hear your voice")
    except sr.RequestError as e:
        print("Request failed")
    return data
    #tts=gTTS(data,lang="fr",tld="fr")
    #tts.save("Speech.mp3")
    #playsound.playsound("Speech.mp3")
#listen()

#now we will create a function to respond back
def respond(String):
    """resopond function"""
    print(String)
    tts=gTTS(String)
    tts.save('speech.mp3')
    filename="Speech%s.mp3"%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
#now we will create our assistant function to make conversation

def va(data):
    """virtual assistant actions"""
    if "how are you" in data:
        listening=True
        respond("I am doing good ,hope you are fine")
    elif "what are your plans" in data:
        listening=True
        respond("yup!!!,not yet planed")
    elif "time" in data:
        listening=True
        respond(time.ctime()) #ctime->current time
    elif "open google" in data.casefold():
        listening=True
        reg_ex=re.search("open google(.*)",data)
        url ="https://www.google.com/"
        if reg_ex:
            sub=reg_ex.group(1)
            url=url+ 'r/'
        webbrowser.open(url)
        respond("successfully done")
    elif "locate" in data.casefold():
        listening=True
        webbrowser.open('https://www.google.com/maps/search/'+data.replace("locate",""))
        respond("Located")
    elif "stop talking" in data:
        listening=False
        respond("okay!!!,cool...")
    try:
        return listening
    except UnboundLocalError:
        print("Time out,you can try again!!!!")
respond("Hey harshitha,how are you?")
#greeting from assistant
listening=True
while listening:
    data=listen()
    listening=va(data)







    
