import google.generativeai as genai
genai.configure(api_key="AIzaSyCx_PErcBmEoZtriY0Iq5On1TWFTUf_MDs")
import pyttsx3
import speech_recognition as sr
import pyaudio
import os
import datetime as dt
import cv2
from requests import get
# import wikipedia needs to be installed
import wikipedia
import webbrowser
import pywhatkit as kit
# lib to mail
import smtplib 
import ssl
import sys
import pyautogui
import time
import requests
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voices",voices[0].id)
# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
# take command using sr lib, pyaudio has been installed as part of sr lib voice to text converter
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        # speak("listening")
        print("listening")
        r.pause_threshold=1
        audio=r.listen(source,timeout=5,phrase_time_limit=5)

    try:
        print("recognizing")
        query = r.recognize_google(audio, language='en-in')
        query=query.lower()
        print(f"user said:{query}")
    except Exception as E:
        speak(" please repeat that ")
        # takeCommand()
        return "none"
    return query

# function to wish goodmorning sir using date time module/
def wish():
    hour = int(dt.datetime.now().hour)
    if hour<12:
        speak("good morning sir")
    elif hour<16:
        speak("good afternoon sir")
    else:
        speak("good evening sir")

def sendMail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("sharmaudita855@gmail.com","dmto100k")
    smtplib.SMTP_SSL
    server.sendmail("sharmaudita855@gmail.com",to,content)
    server.close()
    # context = ssl.create_default_context()
    # with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    #     server.login("sharmaudita855@gmail.com", "dmto100k")
    #     server.send_message(message)


def taskExecution():
    pyautogui.press("esc")
    speak("verification succesful")
    speak("welcome back master Kapil")
    wish()
    while True:
        query=takeCommand()

        if "east or west" in query:
            speak ("AKG is the best")
        elif "the time" in query:
            strtime=dt.datetime.now().strftime("%H:%M")
            speak(f"sir the time is{strtime}")

        
        elif "open spotify" in query:
            cpath="C:\\Users\\kapil\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(cpath)
        # terminal
        elif "open terminal" in query:
            os.system("start cmd")
        elif "introduce" in query:
            speak("i am jarvis. i have been created by Kapil Agnihotri using a total of 20 python libraries")
            speak(".My capabilities include facial recognition, playing yt videos, opening and closing apps, searching the web.")
        # camera
        elif "open camera"in query:
            cam=cv2.VideoCapture(0)
            while True:
                ret,img=cam.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(50)
                if k==27:
                    break
            cam.release()
            cv2.destroyAllWindows()
            
        # ip add
        elif "ip address" in query:
            ip=get('https://api.ipify.org').text
            print(ip)
            speak(f"your ip address is :{ip}")
        # wikipedia
        elif "wikipedia" in query:
            speak("searching wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)
            # print (results)
        # elif "youtube" in query:
        #     webbrowser.open("youtube.com")
        # internet
        elif "search the internet" in query:
            speak("what should i search for")
            cm=takeCommand().lower()
            webbrowser.open(f"{cm}")
        elif "send message" in query:
            kit.sendwhatmsg("+917999722712", "sup", 18, 7)
            print("Message scheduled successfully!")
        # fix english, now it is ply youtube songname
        elif "play on youtube" in query:
            query=query.replace("play on youtube","")
            print(query)
            kit.playonyt(f"{query}")
        # not working properly login error 
        elif "email to kapil" in query:
            try:
                speak("what should i say")
                # sendMail(to,content)
                content=takeCommand().lower()
                to="kapilagnihotri101@gmail.com"
                sendMail(to,content)
                speak("email sent")
            except Exception as e:
                print(e)
                speak("no possible")
        # switch tab
        elif "change tab" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        # code to scroll down
        elif "scroll d" in query:
            # pyautogui.keyDown("fn") 
            pyautogui.press("pagedown")
            time.sleep(1)
        # code to scroll up
        elif "scroll u" in query:
            pyautogui.press("pageup")
            time.sleep(1)

        # use gemini

        elif "use generative ai" in query:
            speak("getting gemini AI by google")
            speak("what should i draft")
            c=takeCommand().lower()
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(c)
            print(response.text)
            speak(response.text)
        # code to create boiler plate in html
        elif "html" in query:
            pyautogui.keyDown("ctrl")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("ctrl")
            pyautogui.keyDown("shift")
            pyautogui.press("1")
            time.sleep(1)
            pyautogui.keyUp("shift")
            pyautogui.press("enter")
            time.sleep(1)



        # screenshot
        elif "screenshot" in query:
            speak("sir tell me the file name to save the screenshot")
            name=takeCommand().lower()
            speak("hold the screen while i take the screenshot")
            time.sleep(3)
            img=pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("screenshot saved")

        # terminate prog
        elif "terminate program" in query:
            speak("exiting task")
            # speak("going to standby mode")
            # break
            sys.exit()
        # system sleep
        elif "system sleep" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            sys.exit()

        # system shutdown
        elif "system shutdown" in query:
            os.system("shutdown /s /t 5")


       


###########################################################################################################
import cv2

recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
recognizer.read('trainer/trainer.yml')   #load trained model
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath) #initializing haar cascade for object detection approach

font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type


id = 2 #number of persons you want to Recognize


names = ['','kapil']  #names, leave first empty bcz counter starts from 0


cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #cv2.CAP_DSHOW to remove warning
cam.set(3, 640) # set video FrameWidht
cam.set(4, 480) # set video FrameHeight

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

# flag = True

while True:

    ret, img =cam.read() #read the frames using the above created object

    converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #The function converts an input image from one color space to another

    faces = faceCascade.detectMultiScale( 
        converted_image,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a rectangle on any image

        id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) #to predict on every single image

        # Check if accuracy is less them 100 ==> "0" is perfect match 
        if (accuracy < 70):
            id = names[id]
            accuracy = "  {0}%".format(round(100 - accuracy))
            taskExecution()

        else:
            id = "unknown"
            accuracy = "  {0}%".format(round(100 - accuracy))
            speak("access denied user is not master Kapil")
        
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
    cv2.imshow('camera',img) 

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

# Do a bit of cleanup
print("Thanks for using this program, have a good day.")
cam.release()
cv2.destroyAllWindows()


if __name__== "__main__":
    while True:
        permission=takeCommand()
        if "activate" in permission:
            taskExecution()
        elif "offline"in permission:
            speak("thank you sir")
            speak("exiting program")
            sys.exit()
       

