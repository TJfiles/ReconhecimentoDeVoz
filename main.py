import speech_recognition as sr

#Pyaudio file (PyAudio-0.2.11-cp38-cp38-win_amd64.whl) was downloaded from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
#the project folder and then installed via https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio


def get_audio():
    listener = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as source:
                print('Listening...')
                audio = listener.listen(source)
                texto = listener.recognize_google(audio, language='en-US')
                texto = texto.lower()
                return texto
        except:
            print("Please Repeat")
            pass

text = get_audio()
print(text)