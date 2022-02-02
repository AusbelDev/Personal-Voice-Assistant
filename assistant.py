
from re import search
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

def search_web(input):

    driver = webdriver.Firefox()
    driver.implicitly_wait(1)
    driver.maximize_window()

    if 'youtube' in input.lower():
        assistant_talks('Opening in youtube')
        indx = input.lower().split().index('youtube')
        query = input.split()[indx + 1:]
        driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query))
        return

    elif 'wikipedia' in input.lower():
        assistant_talks('Opening Wikipedia')
        indx = input.lower().split().index('wikipedia')
        query = input.split()[indx + 1:]
        driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))
        return

    else:
        if 'google' in input:
  
            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            driver.get("https://www.google.com/search?q =" + '+'.join(query))
  
        elif 'search' in input:
  
            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            driver.get("https://www.google.com/search?q =" + '+'.join(query))
  
        else:
  
            driver.get("https://www.google.com/search?q =" + '+'.join(input.split()))
  
        return
