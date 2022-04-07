import pyttsx3
import datetime 
import speech_recognition as sr
import webbrowser as wb
import os


friday=pyttsx3.init()
voices = friday.getProperty('voices')
friday.setProperty('voice', voices[1].id) 

def speak(audio):
    print('Assistant ' + audio)
    friday.say(audio)
    friday.runAndWait()
#speak(..)   
    
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%p") 
    speak("It is")
    speak(Time)

def welcome():
        #Chao hoi
        hour=datetime.datetime.now().hour
        if hour >= 6 and hour<12:
            speak("Good Morning Madam!")
        elif hour>=12 and hour<18:
            speak("Good Afternoon Madam!")
        elif hour>=18 and hour<24:
            speak("Good Evening Madam")
        speak("How can I help you,boss") 


def command():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold=2 #dừng 2s trc khi nhận lệnh mới
        audio=c.listen(source)
    try:
        query = c.recognize_google(audio,language='en-US')
        print("Miss Huyen: "+query)
    except sr.UnknownValueError:
        print('Sorry madam! I didn\'t get that! Try typing the command!')
        query = str(input('Your order is: '))
    return query

if __name__  =="__main__":
    welcome()

    while True:
        query=command().lower()
        #All the command will store in lower case for easy recognition
        if "google" in query:
            speak("What should I search,boss")
            search=command().lower()
            url = f"https://google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on google')
        
        elif "youtube" in query:
            speak("What should I search,boss")
            search=command().lower()
            url = f"https://youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on youtube')
        elif "open video" in query:
            meme =r"C:\Users\Admin\Desktop\test\meme.mp4"
            os.startfile(meme)
        elif 'time' in query:
            time()
        elif "quit" in query:
            speak("Assistant is off. Goodbye boss")
            quit()