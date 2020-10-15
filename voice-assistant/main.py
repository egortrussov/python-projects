import speech_recognition as sr 
import webbrowser

import time

from time import ctime


r = sr.Recognizer()

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)

        audio = r.listen(source)
        print(audio)

        voice_data = ''

        try:
            voice_data = r.recognize_google(audio, language = 'en-IN' )
        except sr.UnknownValueError:
            print('Im a dumbass and didnt get it')
        except sr.RequestError:
            print('Sorry my brain is down')
        
        return voice_data

def respond(voice_data):
    if 'cake' in voice_data:
        print('I dont have a cake cook yourself')
        return;
    if 'what' in voice_data:
        if 'time' in voice_data:
            print(ctime())
        return;
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search 
        webbrowser.get().open(url)
        print('Heres wjat i found for ' + search)
        return;
    if 'location' in voice_data:
        location = record_audio('What do you want me to find?')
        url = 'https://google.nl/maps/place/' + location + '/&amp' 
        webbrowser.get().open(url)
        print('Theres the place you look for')
        return;
    if 'stop' in voice_data:
        exit()

time.sleep(1) 

print('wat do u want')

while (1):
    voice_data = record_audio()

    print(voice_data)

    respond(voice_data)
    print('Ask something else')

