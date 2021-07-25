import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import requests
from bs4 import BeautifulSoup
import instaloader
import PyPDF2

from requests import get





engine = pyttsx3.init('sapi5')  
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<3:
       speak("Hello")
    if hour>=3 and hour<=12:
       speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    
    speak("I am..honey..Please tell me..how may I help you?")

def takeCommand():
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1

        
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query
        
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email','your-password-here')
    server.sendmail('email', to, content)
    server.close()

def pdf_reader():
    book=open('name.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(book) 
    pages = pdfReader.numPages
    speak(f"Total numbers of pages in this file {pages}")
    speak("Please enter the page number you want me to read")
    pg = int(input("Please enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)
if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query= query.replace("wikipedia","")
            results= wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query: 
            webbrowser.open("youtube.com")
        elif 'open google' in query: 
            webbrowser.open("google.com")
      
        
        elif 'open instagram profile' in query:
            speak("please enter the username correctly.")
            name = input("Enter username here:")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"here is the profile of the user {name}")
            speak(f"would you like to download profile picture of this account")
            condition = takeCommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name,profile_pic_only=True)
                speak("profile picture saved in our main folder, now i am ready for next command")
            else:
                pass    

        elif 'play music' in query:
            music_dir= "D:\\music"
            songs= os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"love,the time is {strTime}")
        elif 'whatsapp' in query:
            codePath="C:\\Users\\Taniya Chakaraborty\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(codePath)

        elif 'my instagram profile' in query: 
            webbrowser.open("instagram.com")
        elif 'email to harshit' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "xyz@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                #print(e)
                speak("Sorry not able to sent this Email at this moment")
        elif 'temperature' in query:
            search = "temperature in gwahati"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div" , class_="BNeawe").text
            speak(f"current {search} is {temp}")
        elif 'read pdf' in query:
            pdf_reader()
        elif 'ip address' in query:
                    ip = get('https://api.ipify.org').text
                    speak(f"your ip address is {ip}")
            
        

        

