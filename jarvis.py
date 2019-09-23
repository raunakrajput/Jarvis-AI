import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import requests



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
     hour=int(datetime.datetime.now().hour)
     if hour>=0 and hour<12:
          speak("Good Morning!")
     elif hour>=12 and hour<18:
          speak("Good Afternoon!")
     else:
          speak("Good Evening!")
     speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():

     r = sr.Recognizer()
     with sr.Microphone() as source:
          print("Listening...") 
          r.pause_threshold=1  
          audio=r.listen(source)

     try:
          print("Recognizing...")  
          query=r.recognize_google(audio, language='en-in') 
          print(f"User said: {query}\n")  

     except Exception as e:
          print(e)

          print("Say that again please...")
          return "Null"
     return query

def currencyConverter():
     currencyFrom=input("Enter Currency to convert From : ")
     url = 'https://api.exchangerate-api.com/v4/latest/'+currencyFrom
     response = requests.get(url)
     lines = response.json()
     for line in lines:
          country=lines["rates"]
     amount=int(input("Enter amount: \n"))
     print("Enter the name of currency you want to convert this amount to? "
      "Available options:\n")
     [print(item) for item in country.keys()]
     currency=input("Please enter one of these values :\n")
     print(f"{amount} {currencyFrom} is equal to {amount*float(country[currency])} {currency}")


if __name__=="__main__":
     wishMe()
     while True:
          query=takeCommand().lower()
     
          if 'wikipedia' in query:

               speak("Searching Wikipedia...")
               query=query.replace("wikipedia","")
               results=wikipedia.summary(query,sentences=2)
               speak("According to wikipedia")
               print(results)
               speak(results)
          elif 'open youtube' in query:
               webbrowser.open("youtube.com")

          elif 'open google' in query:
               webbrowser.open("google.com")

          elif 'open stackoverflow' in query:
               webbrowser.open("stackoverflow.com")
          
          elif 'play music' in query:
               music_dir = 'D:\\Song'
               songs=os.listdir(music_dir)
               print(songs)
               os.startfile(os.path.join(music_dir,songs[0]) )
          
          elif 'the time' in query:
               strTime=datetime.datetime.now().strftime("%H:%M:%S")
               print(strTime)
               speak(f"Sir the time is {strTime} ")

          elif 'open code' in query:
               codePath='"C:\\Users\\rauna\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"'
               os.startfile(codePath)

          

          
          
          #talk function

          elif 'good morning' in query:
               hour=int(datetime.datetime.now().hour)
               if hour<=0 and hour>12:
                  speak("Good Morning Sir!")
               elif hour<=12 and hour>18:
                  speak("Sir its Good afternoon!")
               else:
                    speak("Sir its good evening1")


          elif 'good afternoon' in query:
               hour=int(datetime.datetime.now().hour)
               if hour<=0 and hour>12:
                  speak("Good Morning Sir!")
               elif hour<=12 and hour>18:
                  speak("Sir its Good afternoon!")
               else:
                    speak("Sir its good evening1")
              

          elif 'good evening' in query:
               hour=int(datetime.datetime.now().hour)
               if hour<=0 and hour>12:
                  speak("Good Morning Sir!")
               elif hour<=12 and hour>18:
                  speak("Sir its Good afternoon!")
               else:
                    speak("Sir its good evening1")

          elif 'good night' in query:
               hour=int(datetime.datetime.now().hour)
               if hour<=0 and hour>12:
                  speak("Good Morning Sir!")
               elif hour<=12 and hour>18:
                  speak("Sir its Good afternoon!")
               
               
               else:
                    speak("Good Night Sir! sweet dream")
          
          
          elif '007 stop stop' in query:
               break
          
          elif 'open ucurrency converter' in query:
               currencyConverter()

               
          
          
          
          
               

            
            
               
               

           
