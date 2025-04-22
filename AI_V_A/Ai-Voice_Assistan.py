import speech_recognition as sr
import pyttsx3    

engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def listen():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try:
            text=recognizer.recognize_google(audio)
            print("You said: ",text)
            return text.lower()
        except sr.UnknownValueError:
            print("Sorry, I could not understand.")
            return None

def process_command(command):
    if "hello" in command:
        speak("hello! How can I assist you Rashmi Ranjan Behera?")
    elif "your name" in command:
        speak("I am Your A I Assistant.")
    elif "exit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I couldn't understand")

while True:
    user_command =listen()
    if user_command:
        process_command(user_command)

