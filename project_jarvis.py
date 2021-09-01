import pyttsx3  # it is text to speach conversion library import to use speak function
import datetime
import speech_recognition as sr  # to take input voice cammand and convert in text
import wikipedia
import webbrowser  # so we can access web page and browse command
import os  # for opening app through command
import random  # we use random module for playing random song
import colorama
from colorama import Fore
from colorama import Style
import psutil  # it gives information of running process and system utilization (memory,cpu,battery)
import pyjokes  # import jokes library
import pyautogui
import time  # coz we have use time to stop listen by assistence
# import winsound  this default library to play song in python
from playsound import playsound

engine = pyttsx3.init('sapi5')  # sapi 5 is developed by microsoft to use speech recognition
voice = engine.getProperty('voices')
# print(voice[1].id) or print(voice[1].id)  coz in pc two voices are installed only
engine.setProperty('voice', voice[0].id)  # it's set the voice which we are using among the 2
engine.setProperty('rate', 170)  # it is use to decrease the speed of voice coz default one is very fast


def speak(audio):  # we input some text which is speak by assistence
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    speak('Welcome back Mahesh sir')
    hour = int(datetime.datetime.now().strftime('%H'))
    if hour >= 0 and hour <= 12:
        engine.say("GOOD MORNING!! It's " + str(
            hour) + "am")  # we can use speak function bt we cannot add variable content then
        engine.runAndWait()
    elif hour >= 12 and hour <= 18:
        engine.say("GOOD AFTERNOON!! It's " + str(
            hour) + "pm")  # we can use speak function bt we cannot add variable content then
        engine.runAndWait()
    else:
        engine.say("GOOD EVENING!! It's " + str(
            hour) + "pm")  # we can use speak function bt we cannot add variable content then
        engine.runAndWait()
    date = datetime.date.today()
    speak('The current date is'+str(date))
    speak(" i am jarvice!!How May I help You?")


def takeCommand():  # this function is used to input voice command and return it into text
    r = sr.Recognizer()  # its the function of sr which access the classes like recognize_google() which have access to web page
    with sr.Microphone() as source:  # here we take the input voice command in source
        # winsound.Beep(1000,60)   this uses default bepp sound in windows
        print(Fore.GREEN + Style.BRIGHT + "Listening.......")
        playsound(r'C:\Users\DELL\Music\songs\pop.mp3')
        r.pause_threshold = 1  # it's the minimum time of user take pause before completing command
        audio = r.listen(source)
    try:
        print(Fore.CYAN + Style.BRIGHT + "Recognizing......." + Style.RESET_ALL)
        query = r.recognize_google(audio, language='en - in')  # its method of Recognizer function which access google web page
        print(Fore.RED + Style.BRIGHT + f"User Said:- {query}\n")
    except Exception as e:
        #  print(e)
        speak("Sat It Again!!!")
        return "NONE"
    return query


def cpu():
    usage = str(psutil.cpu_percent())  # it tells the cpu usage
    speak('CPU is at' + usage)

    battery = psutil.sensors_battery()  # we didn't convert into str bcoz then it does not speak battery percent it speak all useless data
    speak('BATTERY is at')  # it gives current battery percentage
    speak(battery.percent)


def jokes():
    speak(pyjokes.get_joke())


def screenshot():
    img = pyautogui.screenshot()
    img.save(r'C:\Users\DELL\OneDrive\Pictures\Screenshots\jarvis.PNG')
    speak("screenshot has been taken")
    # also it can can be done by another way
    # img_loc = r'C:\Users\DELL\OneDrive\Pictures\Screenshots\.PNG'
    # pyautogui.screenshot(imageFilename=img_loc)


if __name__ == "__main__":
    #wishMe()
    while True:
        query = takeCommand().lower()      # logic for executing task takes command in query variable lower convert voice command in small letters

    # if 1:  we can use bt it will run only one time

        if 'wikipedia' in query:  # we called wikipedia word in command
            speak('searching wikipedia!!!!!')
            query = query.replace("wikipedia", '')  # after recognizing wikipedia in query we remove wikipedia word from command cause it's while loop its repetatly runs querry
            result = wikipedia.summary(query, sentences=2)
            print(Fore.BLUE + Style.BRIGHT + result)
            speak(result)

        elif 'who are you' in query or 'what is your name' in query:
            speak("i am, jarvice version 4.0!!Created by,mahesh godse on 11 May 2021")

        elif 'who created you' in query or 'who is your creator' in query:
            speak("Thanks To Mahesh Sirr!!They Created Me to Work As AI Dekstop assistence on 11 May 2021pip ")

        elif 'how are you' in query:
            speak('i am fine sir!!thats sweet of you,and hopefully you are also doing well!!!')

        elif 'open chrome' in query:
            speak('opening chrome!!')
            webbrowser.open('chrome.com')

        elif 'open youtube' in query:
            speak('what should i search')
            search = takeCommand().lower()
            speak('opening youtube!!!')
            webbrowser.open('https://www.youtube.com/results?search_query='+search)  # its open and brows youtube on webpage

        elif 'open google' in query:
            speak('what should i search on google?')
            search_google = takeCommand().lower()
            speak('opening google')
            webbrowser.open('https://www.google.co.in/search?q='+search_google)

        elif 'play music' in query:
            speak("playing music")
            Music_path = 'C:\\Users\\DELL\\Music\\songs'  # path off songs folder
            songs = os.listdir(Music_path)  # it add all songs and make its list
            random_song = random.randint(0, len(songs) - 1)  # we use random module for playing random song
            print(Fore.YELLOW + Style.BRIGHT + "\t[Now Playing....", songs[random_song], "]")
            os.startfile(os.path.join(Music_path, songs[random_song]))  # its method of os

        elif 'open spotify' in query:
            speak('opening spotify')
            webbrowser.open('spotify.com')

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak('Sir,The Time is' + strTime)

        elif 'open code' in query:
            speak('opening  microsoft vs code')
            vs_path = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vs_path)

        elif 'open microsoft teams' in query:
            speak('opening microsoft teams ')
            team_path = r'C:\Users\DELL\AppData\Local\Microsoft\Teams\Update.exe --processStart "Teams.exe"'
            os.system(team_path)

        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            path = 'C:\\Users\\DELL\\AppData\\Local\\WhatsApp\\WhatsApp.exe'
            os.startfile(path)  # its starts file at this path

        elif 'cpu' in query:
            print('analysing cpu....')
            speak('analysing cpu....')
            cpu()

        elif 'joke' in query:
            jokes()
            speak('hehehehe it was very funny')

        elif 'go offline' in query:
            speak('signing off!!')
            quit()

        elif 'word' in query:
            speak('opening ms word!!!')
            word_path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(word_path)

        elif 'write a note' in query:
            speak('what should i write sir!!!')
            notes = takeCommand()
            file = open('notes.txt', 'a')
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak('should i mentioned date and time sir?')
            ans = takeCommand().lower()

            if 'yes' in ans or 'sure' in ans or 'ok' in ans:
                file.write(strTime + ':\n')
                file.write('\t' + notes + '\n')
                file.close()
                speak('Note has been taken sir!!')

            else:
                file.write(strTime + ':\n')
                file.write('\t' + notes + '\n')
                file.close()
                speak('note has been taken sir!!')

        elif 'show notes' in query:
            file = open('notes.txt', 'r')
            print(Fore.YELLOW + Style.BRIGHT + file.read())
            file.close()

        elif 'delete notes' in query:
            file = open('notes.txt', 'w')
            file.write('')
            speak('notes has been cleared sir!!')
            print(Fore.GREEN + Style.BRIGHT + '\tNotes deleted successfully!!'+Style.RESET_ALL)

        elif 'screenshot' in query:
            screenshot()

        elif 'where is' in query:
            query = query.replace('where is', '')  # by replacing where is with null we can take only location that user said 
            location = query  # here we have only location said by user
            print(Fore.YELLOW + Style.BRIGHT + "user asks to locate:-", location)
            webbrowser.open_new_tab(r'https://www.google.co.in/maps/place/'+location)

        elif 'stop listening' in query:
            speak('how many seconds do i stop to listen your commands!!!')
            timeout = int(takeCommand())
            speak('system goes offline for' + str(timeout) + 'seconds')
            print(Fore.YELLOW+Style.BRIGHT+'System Go online After ', timeout, "s")
            time.sleep(timeout)

        elif 'sleep' in query:
            os.system("shutdown -l")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        else:
            speak('here are some results from google')
            webbrowser.open('https://www.google.co.in/search?q=' + query)

