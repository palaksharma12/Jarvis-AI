from typing import Mapping
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import smtplib
import datetime
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1])
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon ")
    else:
        speak("Good Evening!")

    speak("I am jarvis. Please tell me how can I help you?")
def takeCommand():
    # it takes microphone input from user and returns string output

    r=sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recogizing...")
        query=r.recognize_google(audio,language='en-in')
        print("user said : ", query)

    except Exception as e:
        # print(e)

        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('b20159@students.iitmandi.ac.in','poom@nnu7')
    server.sendmail('b20159@students.iitmandi.ac.in',to,content)
    server.close()



if __name__=="__main__":
    wishMe()
    while(True):
#    if(1):
        query=takeCommand().lower()
        

    #logic for executing task based on query

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query= query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'play music' in query:
            music_dir='D:\\music'
            songs=os.listdir(music_dir)
            print(songs) 
            os.startfile(os.path.join(music_dir,songs[0]))

        elif "time" in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strtime}")
            
        elif "open code" in query:
            codepath="C:\\Users\\PALAK SHARMA\\Desktop\\mycodes\\cp.exe"
            os.startfile(codepath)
        
        elif "send email" in query:
            d={'palak':'plksharma12@gmail.com','pooja':'pinkusharma7575@gmail.com','poonam':'sharmapoonam10000@gmail.com'}
            try:
                speak("To whom I have to send")
                name=takeCommand()
                speak("What should I say")
                content=takeCommand()
                if 'palak' or "palk" or 'plk' in name:
                    to=d['palak']
                elif 'pooja' or 'puja' in name:
                    to=d['pooja']
                elif 'punam' or "poonam" in name:
                    to=d['poonam']
                
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry found some conflict in sending mail. Please try again")

        elif "quit" in query:
            break



