import speech_recognition as sr 

from time import ctime


r = sr.Recognizer()

def record_audio():
    with sr.Microphone() as source:
        audio = r.listen(source)
        print(audio)

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
    if 'what' in voice_data and 'time' in voice_data:
        print(ctime())

print('wat do u want')

voice_data = record_audio()

print(voice_data)

respond(voice_data)