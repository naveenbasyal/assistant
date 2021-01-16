import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import pafy

import pywhatkit as kit

import re
import pyaudio
from pygame import mixer
import time
from playsound import playsound
from urllib.request import urlopen
import pyjokes
from subprocess import run
import random
from gtts import gTTS
from twilio.rest import Client
import json
import requests
import wolframalpha
import ctypes
import smtplib
import subprocess



print('Loading your AI personal assistant - LMS')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')



def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning")
        print("Good Morning")
    elif hour>=12 and hour<17:
        speak("Good Afternoon")
        print("Good Afternoon")
    else:
        speak("Good Evening")
        print("Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:

        print("I Am Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en')
            print(f"user said:{statement}\n")

        except Exception as e:
            statement=takeCommand()

        return statement


speak(" Loading your AI personal assistant :  ")
speak("hello , i am lucifer morning star")
wishMe()

speak("Tell me ,how Can i Help You Sir: ")


if __name__=='__main__':


    while True:

        statement = takeCommand().lower()
        if statement==0:
            continue



        if 'who is' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            time.sleep(1)

        if 'do you know' in statement:
            speak('Searching my brain...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=2)
            speak("According to my brain")
            print(results)
            speak(results)
            time.sleep(1)

        elif "you are not smart" in statement or " you are slow " in statement or "you are stupid" in statement or "you are bad" in statement:
            speak("sorry : is i said something wrong?:  it may be connectivity issue or some mic issue.")

        elif "you are so talented" in statement or "you are smart" in statement or "i am impressed" in statement  or "you are nice"in statement or "you are great"in statement:
            speak("well , thanks: i think its just because Master Naveen made me")

        elif "stop talking" in statement or "shut up" in statement  or "get out"in statement or "shut you mouth"in statement :
            speak("well ,  i can do that  sir ")
            speak("can you say (sign out) or (stop now) ")

        elif "hello" in statement  or "hi "in statement:
            speak("hi sir , i am waiting for your command")

        elif "goodafternoon" in statement:
            speak("goodafternoon sir")

        elif "goodevening" in statement:
            speak("goodevening sir")

        elif "goodmorning" in statement :
            speak("goodmorning sir")

        elif  "where are you "in statement or "are you here? "in statement or "luci " in statement or "lucifer" in statement or "hay" in statement:

            speak(" lucifer morning star in your service ")
            speak("waiting for you command")

        elif "go to my youtube channel" in statement or "open my youtube channel" in statement or "where is my youtube channel" in statement:
            speak("going to your channel")
            webbrowser.open("https://www.youtube.com/channel/UCvNzTsSWN7Nr3LzJdfjlWIQ?view_as=subscriber")
            time.sleep(3)
            speak("here is your youtube channel, named : soul naveen y  t")
            time.sleep(3)

        elif 'open youtube' in statement:
            speak("opening youtube")
            webbrowser.open_new_tab("https://www.youtube.com")
            time.sleep(2)
            speak("youtube is open now")
            speak("Uploading and watching videos on YouTube is completely free. Gives you the opportunity to earn money through your videos")
            time.sleep(3)

        elif 'open youtube' in statement:
            speak("opening youtube")
            webbrowser.open_new_tab("https://www.youtube.com")
            time.sleep(2)
            speak("youtube is open now")
            time.sleep(2)


        elif "don't listen" in statement or "stop listening" in statement:

            speak("for how much time you want to stop me from listening commands")
            a = int(takeCommand())
            speak(f"okay sir: i will stop listening for {a} seconds")
            speak("the time starts now: ")
            time.sleep(a)
            print(f"Waiting for {a} Seconds......")
            speak(f"Time up sir : {a} seconds completed : how can i help you")

        elif 'open google' in statement:
            speak("ok, opening google chrome")
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            speak("Chrome is an extremely fast web browser; it loads and displays pages very quickly. You can drag tabs out into separate windows, without difficulty, and back in again with your mouse.")
            time.sleep(1)


        elif 'say something' in statement:
            speak("okay, What should i say : ?")
            statement=takeCommand().lower()
            print("G-one : "+statement)
            speak(statement)
            speak("want to say me more")
            a=takeCommand().lower()
            if "yes" in a:
                speak("okay, what should i say")
                statement=takeCommand().lower()
                print("G-one : " + statement)
                speak(statement)
            else:
                speak("okay then! i am in your service ")


        elif 'open gmail' in statement:
            speak("opening gmail")
            webbrowser.open_new_tab("https://www.gmail.com")
            time.sleep(4)
            speak("Google Mail open now")
            time.sleep(1)



        elif 'how are you' in statement:
            speak("I am fine, Thank you for asking ")
            speak("by the way, How are you, Sir")


        elif "restart" in statement:
            subprocess.call(["shutdown", "/r"])

        elif 'fine' in statement or "good" in statement:

            speak("It's good to know that your fine")
            time.sleep(1)

        elif 'open my gmail' in statement or "my gmail account" in statement or "where is my mail" in statement:

            speak("going to your gmail account")
            webbrowser.open_new_tab("https://mail.google.com/mail/u/2/#inbox")
            time.sleep(3)
            speak("here is your gmail account")
            time.sleep(2)


        elif 'whats the time' in statement or 'tell me the time' in statement or 'what time is it' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            print(strTime)
            time.sleep(2)

        elif "write a note" in statement:
            speak("What should i write, sir")
            statement = takeCommand().lower()
            file = open('jarvis.txt', 'w')
            file.write(statement)
            speak(" sir,your note has been written")

        elif "show note" in statement or "show my notes"in statement or "read notes" in statement:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read())

        elif 'who are you' in statement  or 'introduce youself' in statement:
            speak('hi,I am Lucifer Morning star ,  speed 1 tera hertz ,memory 1 zetabyte : your personal assistant: I am programmed using python : ')
            time.sleep(1)

        elif 'what can you do' in statement or "tell me about your features" in statement or "what are your capabilities" in statement:
             speak('i can do various things like,'
                  ': opening youtube : google chrome: gmail : stackoverflow : github : predict time: i can also search wikipedia' 
                  ': i can get top headline news from times of india : i can lock : restart : or shutdown your system , i can play music and lot more')

        elif 'shutdown system' in statement:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                os.system("shutdown /s /t 1")

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak(" I started out as an idea , then one day : Master Naveen , helped bring me to life!!")
            print("LMS: I Started out as an idea , then one day : Master Naveen , helped bring me to life!!")
            time.sleep(2)



        elif 'joke' in statement:

            res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept": "application/json"}
            )
            if res.status_code == requests.codes.ok:
                speak(str(res.json()['joke']))
            else:
                speak('oops!I ran out of jokes')


        elif "your boss" in statement:
            speak("well:  right now you are my boss,i can do anything you want me to do ")


        elif "how to" in statement:
            statement = statement.split("for")[-1]
            url = f"https://google.com/search?q={statement}"
            webbrowser.get().open(url)
            speak(f'Here is what I found for {statement} on google')



        elif 'search'  in statement:
            statement= statement.split("for")[-1]
            url = f"https://google.com/search?q={statement}"
            webbrowser.get().open(url)
            speak(f'Here is what I found for {statement} on google')


        elif "set a timer" in statement:
            speak("okay, For How long:?? ")
            a=takeCommand().lower()
            speak(f"awesome, i will wake you up after {a} seconds")
            time.sleep(int(a))
            speak("sir : please wake up"*14)

        elif "open my github" in statement or "open git" in statement or "open github" in statement  :
            speak("going to your (git) account")
            webbrowser.open_new_tab("https://github.com/naveen021-max")
            time.sleep(1)
            speak("here is your github account : Git allows and encourages you to have multiple local branches, that can be entirely independent of each other. The creation, merging, and deletion of those lines of development takes seconds. ")



        elif 'lock window' in statement:

            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()
            time.sleep(1)

        elif 'wait a minute'  in statement:
            speak("ok , i am waiting for a minute")
            print(" Waiting For 1 minute.....")
            time.sleep(60)
            print("Time Over!!!!!")
            speak(": Time Over Sir")


        elif "who i am" in statement:
            speak("If you talk then definately your human.")



        elif 'news' in statement    :
            speak('going to show you some headlines')
            webbrowser.open("https://timesofindia.indiatimes.com/home/headlines")
            time.sleep(2)
            speak("here are some headlines from times of india ,: happy reading!!")


        elif 'wait for 5 minutes'  in statement:
            speak("ok , i am waiting for 5 minutes and then,i will ask you for my help")
            print(" Waiting For 5 minutes.....")
            time.sleep(300)
            print(" Time Over!!!!!")
            speak(": Time Over Sir")

        elif "open powerpoint" in statement or "open ppt" in statement:
            speak("opening powerpoint")
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office PowerPoint 2007")


        elif 'wait a second' in statement:
            speak("ok , i am waiting for 15 seconds")
            print(" Waiting For 15 Seconds.....")
            time.sleep(15)
            print(" Time Over!!!!!")
            speak(": Time Over Sir")

        elif "play music on youtube" in statement or "play song on youtube":
            speak("how much time you want to listen music, sir (please tell in seconds)")
            a=takeCommand()
            kit.playonyt("sirazee")
            time.sleep(a)

        elif "open notepad" in statement or "open note" in statement:
            speak("okay,opening notepad")
            os.startfile("C:\\Users\\parkash\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad")

        elif "play my favourite music" in statement or "play my favourite song" :
            speak("sir: for how much time , in seconds, you want to listen your favourite music")
            t_m=takeCommand()
            speak("playing your favourite song : ")
            music="C:\Music"
            songs=os.listdir(music)
            print(songs[9])
            speak("(Enjoy the music!!)")
            random_music = random.choice(music)
            random=os.startfile(os.path.join(music,songs[9]))
            time.sleep(int(t_m))




        if "stop now" in statement or "sign out" in statement or "bus karo"  in statement :
                 speak("okay sir, as you wish : lucifer morning star is now going offline")
                 break

















