
#ttest
from re import search
from selenium import webdriver
import os
import speech_recognition as sr
from gtts import gTTS
import wolframalpha
import pyaudio
from pydub import AudioSegment
from pydub.playback import play
from windows_tools.installed_software import get_installed_software


file_num = 1

def assistant_talks(output):
    global file_num

    file_num += 1
    print('Assist: ', output)

    textToSpeak = gTTS(text=output, lang='en', slow=False)

    file = str(file_num) + '.mp3'

    textToSpeak.save(file)
    sound = AudioSegment.from_mp3(file)
    play(sound)
    
    os.remove(file)

def get_audio():

    recorder = sr.Recognizer()
    recorder.energy_threshold = 50
    audio = ""

    with sr.Microphone( device_index=3 ) as source:
        
        print("Speak")

        audio = recorder.listen(source, phrase_time_limit=5)

    print("Stop")
    print(audio)

    try:
        text = recorder.recognize_google(audio, language='en-US')
        print("You : ", text)
        return text
    except sr.UnknownValueError:
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

def open_app(input):
  
    if "firefox" in input or "mozilla" in input:
        assistant_talks("Opening Mozilla Firefox")
        os.startfile('C:\Program Files\Mozilla Firefox\\firefox.exe')
        return
  
    elif "word" in input:
        assistant_talks("Opening Microsoft Word")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Word 2013.lnk')
        return
  
    elif "excel" in input:
        assistant_talks("Opening Microsoft Excel")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Excel 2013.lnk')
        return
  
    else:
  
        assistant_talks("Application not available")
        return

if __name__ == "__main__":
    assistant_talks("What's your name?")
    name ='Ausbel'
    name = get_audio()
    assistant_talks("Hello, " + name + '.')