import speech_recognition as sr
import webbrowser
from time import ctime #currenttime
import time #thread
import playsound #audio output
import os #for remove method
from gtts import gTTS #google text speeech
import random

r = sr.Recognizer()


def receive_audio(ask=False):
    with sr.Microphone() as audio_input:
        if ask: #if ask is True
            speak(ask)

        audio = r.listen(audio_input)
        voice_data = ''

        try:
            voice_data = r.recognize_google(audio)

        except sr.UnknownValueError:
            speak('Pardon, I did not get that')

        except sr.RequestError:
            speak('Sorry, my speech service is currently down')

        return voice_data


def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en') #audio input from user
    r = random.randint(1, 1000000) #random integer for naming file
    audio_file = 'audio-' + str(r) + '.mp3' #file name
    tts.save(audio_file) #save user audio input
    playsound.playsound(audio_file)
    print(audio_string) #print user input on the terminal
    os.remove(audio_file) #remove file once it printed


def respond(voice_data):
    if 'what is your name' in voice_data:
        speak('My name is Speechtonius')
    if 'what time is it' in voice_data:
        speak(ctime())
    if 'search' in voice_data:
        search = receive_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        if sr.UnknownValueError is True:
            speak("Sorry, I could not hear that.")
        else:
            webbrowser.get().open(url)
            speak('Here is what I found for ' + search)

    if 'find location' in voice_data:
        location = receive_audio('What is the location')
        url = 'https://google.com/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        speak('Here is the location of ' + location)
    if 'exit' in voice_data:
        speak('OK. Bye!')
        exit()


time.sleep(1)

speak('Hey there! How can I help you?')

while 1: #while true/ loop infinitely
    voice_data = receive_audio()
    respond(voice_data)