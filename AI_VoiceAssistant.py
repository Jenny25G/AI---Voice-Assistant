import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def take_command():
    try:
        with sr.Microphone(2) as source:
            print("I'm listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'john' in command:
                command = command.replace('john','')
                print(command)

    except:
        pass
    return command

def talk(text):
    engine.say(text)
    engine.runAndWait()


def run_john():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk("Okay, I'm playing " + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H %M %p')
        print(time)
        talk('Current time is'+time)

    elif 'who is' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'Motivation' in command:
        talk('You Only Live Once')

    elif 'Dream' in command:
        talk('You should explore the world.')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    else:
        talk('Please say the command again')





while True:
    run_john()

