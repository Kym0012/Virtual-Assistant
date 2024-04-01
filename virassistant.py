
import speech_recognition as sr
import wikipedia
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
recognizer = sr.Recognizer()

def cmd():
    with sr.Microphone() as source:
        print('Clearing background noises....please wait')
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print('Done clearing background noises.')
        print('Listening...')
        recorded_audio = recognizer.listen(source)
        print('Done recording...')
        
    try:
        command = recognizer.recognize_google(recorded_audio, language='en-US')
        print('Your message: {}'.format(command))
        wikisearch = wikipedia.summary(command)
        print('Wikipedia Summary: {}'.format(wikisearch))
        engine.say(wikisearch)
        engine.runAndWait()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    except wikipedia.exceptions.PageError:
        print("Sorry, I couldn't find any information on that topic.")
    except wikipedia.exceptions.DisambiguationError as e:
        print("There are multiple possible matches for that topic; {0}".format(e))

cmd()
