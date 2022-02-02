
from selenium import webdriver
import os
import speech_recognition as sr
from gtts import gTTS
import wolframalpha
import pyaudio
import playsound

file_num = 1

def assistant_talks(output):
    global file_num

    file_num += 1
    print('Person : ', output)

    textToSpeak = gTTS(text=output, lang='en', slow=False)

    file = str(file_num) + '.mp3'

    textToSpeak.save(file)

    playsound.playsound(file, True)
    os.remove(file)

def get_audio():

    recorder = sr.Recognizer()
    audio = ""

    with sr.Microphone() as source:
        print("Speak")

        audio = recorder.listen(source, phrase_time_limit=5)

    print("Stop")

    try:
        text = recorder.recognize_google(audio, language='en-US')
        print("You : ", text)
        return text
    except:
        assistant_talks("Could not understand your audio. Try again")
        return 0

