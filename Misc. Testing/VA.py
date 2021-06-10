import os, time, playsound
import speech_recognition as sr
from gtts import gTTS

def speak(text):
    tts = gTTS(text = text, lang = "en")
    filename = "outputs/voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as src:
        audio = r.listen(src)
        said = ""
        try:
            said = r.recognize_google(audio)
            #print(said)
        except Exception as e:
            print("Exception : " + str(e))

    return said

input = get_audio()

if input == "hello":
    speak("hi there!")
elif input == "what is 2 + 2":
    speak("it's 4 you small brain")