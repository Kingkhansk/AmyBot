from Brain.AIBrain import ReplyBrain
from Body.Listen import MicExecution
from Brain.Qna import QuestionsAnswers
import datetime
import pygame
import keyboard
import pyautogui
import pyjokes
import webbrowser
from time import sleep
from games.game import stgame
from games.game import sgame
print("Starting the AMY \n")
webbrowser.open("/home/teamelectro/FYP/TemplateForJarvis/Eyes/index.html")
from Body.Speak import Speak
from Features.Clap import Tester
from Features.Wakeup import WakeupDetected
import random
# from Body.Speak import openeyes
print("Starting the AMY, Wait a few seconds \n")
Speak("Hello, I am Amy, An AI Assistant for Autism Impaired Children")
pygame.init()
# from Main import MainTaskExecution




def MainExecution():
    
    greetings = ["Its nice to meet you","Good to see you","What can I do for you?","I am ready to assist you dear!"]
    G = random.choice(greetings)
    Speak("Hello!")
    Speak(G)
    while True:
        
        Data = MicExecution()
        Data = str(Data).replace(".","")
        
        if len(Data) < 3:
            pass
        elif "what time is it" in Data or "what is the time" in Data or "could you tell me what time it is" in Data or "can you let me know the time, please" in Data or "what's the time" in Data or "could you inform me of the time" in Data or "may i know the time" in Data or "do you happen to know what time it is" in Data:
             now = datetime.datetime.now()
             current_time = now.strftime("%I:%M:%S %p")
             Speak(f"current time is {current_time}")
        
        elif "visit" in Data:
            Nameofweb = Data.replace("visit ","")
            link = f"https://www.{Nameofweb}.com"
            webbrowser.open(link)
        
        elif "launch" in Data:
            Nameofweb = Data.replace("launch ","")
            link = f"https://www.{Nameofweb}.com"
            webbrowser.open(link)
        elif "open" in Data:
            Nameoftheapp = Data.replace("open ","")
            pyautogui.press('win')
            sleep(1)
            keyboard.write(Nameoftheapp)
            sleep(1)
            keyboard.press('enter')
            sleep(0.5)
        elif "start" in Data:
            poems=[r"Poems/Baa-Baa-Black-Sheep-.mp3",r"Poems/WheelsOn-the-Bus.1.mp3",r"Poems\\twinkle-star.mp3"]
            P_choice = random.choice(poems)
            Nameoftheapp = Data.replace("start ","")
            if "poem" in Nameoftheapp:
                pygame.mixer.music.load(P_choice)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
            elif "game" in Nameoftheapp:
                pass
            
        elif 'joke' in Data:
            Speak(pyjokes.get_joke())
                
        elif "read the poem" in Data or "poem" in Data or "start singing a poem" in Data or "start poem" in Data or "Commence poem" in Data or "recite poem" in Data or "begin poem" in Data or "play poem" in Data:
            poems=[
                r"/home/teamelectro/FYP/TemplateForJarvis/Poems/Baa-Baa-Black-Sheep-.mp3",
                r"/home/teamelectro/FYP/TemplateForJarvis/Poems/WheelsOn-the-Bus.1.mp3",
                r"/home/teamelectro/FYP/TemplateForJarvis/Poems/twinkle-star.mp3"]
            P_choice = random.choice(poems)
            pygame.mixer.music.load(P_choice)
            pygame.mixer.music.play()
            
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
                
        
        elif "ba ba black sheep" in Data or "sing ba ba black sheep" in Data or "read ba ba black sheep" in Data or "start singing ba ba black sheep" in Data or "start ba ba black sheep" in Data or "Commence ba ba black sheep" in Data or "recite ba ba black sheep" in Data or "begin ba ba black sheep" in Data:
            poems=r"/home/teamelectro/FYP/TemplateForJarvis/Poems/Baa-Baa-Black-Sheep-.mp3"
            # P_choice = random.choice(poems)
            pygame.mixer.music.load(poems)
            pygame.mixer.music.play()
            
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        
        elif "twinkle twinkle" in Data or "sing twinkle twinkle" in Data or "sing twinkle twinkle little star" in Data or "read twinkle twinkle" in Data or "read twinkle twinkle little star" in Data or "start singing twinkle twinkle" in Data or "start singing twinkle twinkle little star" in Data or "start twinkle twinkle" in Data or "start twinkle twinkle little star" in Data or "Commence twinkle twinkle" in Data or "Commence twinkle twinkle little star" in Data or "recite twinkle twinkle" in Data or "recite twinkle twinkle little star" in Data or "begin twinkle twinkle" in Data or "begin twinkle twinkle little star" in Data:
            poems=r"/home/teamelectro/FYP/TemplateForJarvis/Poems/twinkle-star.mp3"
            # P_choice = random.choice(poems)
            pygame.mixer.music.load(poems)
            pygame.mixer.music.play()
            
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        
        
        
        
        elif "sing wheels on the bus" in Data or "read wheels on the bus" in Data or "start singing wheels on the bus" in Data or "start wheels on the bus" in Data or "Commence wheels on the bus" in Data or "recite wheels on the bus" in Data or "begin wheels on the bus" in Data:
            poems=r"/home/teamelectro/FYP/TemplateForJarvis/Poems/WheelsOn-the-Bus.1.mp3"
            # P_choice = random.choice(poems)
            pygame.mixer.music.load(poems)
            pygame.mixer.music.play()
            
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        
        elif "game" in Data:    
            # games = [
            #     r"/home/teamelectro/FYP/TemplateForJarvis/games/Math Game/index.html" , 
            #     r"/home/teamelectro/FYP/TemplateForJarvis/games/Menja/index.html" , 
            #     r"/home/teamelectro/FYP/TemplateForJarvis/games/memory-game/index.html"]
            # g_choice = random.choice(games)
            Speak(f"Starting Random Game")
            # webbrowser.open(g_choice)
            stgame()

        elif "Math game" in Data:
            game = r"/home/teamelectro/FYP/TemplateForJarvis/games/Math Game/index.html"
            Speak("Starting Math Game")
            webbrowser.open(game)
            # sgame("file:///home/teamelectro/FYP/TemplateForJarvis/games/MathGame/index.html")


        elif "Memory game" in Data:
            game = r"/home/teamelectro/FYP/TemplateForJarvis/games/memory-game/index.html"
            Speak("Starting memory Game")
            webbrowser.open(game)
        elif "Menja game" in Data or "Menja" in Data:
            game = r"/home/teamelectro/FYP/TemplateForJarvis/games/Menja/index.html"
            Speak("Starting Menja Game")
            webbrowser.open(game)
        elif "what is your name" in Data or "tell me your name" in Data:
            G = ["I am Amy your friend,","My name is Amy","People call me Amy dear","I am Amy"]
            G_choice = random.choice(G)
            Speak(G_choice)
    
        
        elif "who made you" in Data or "who invented you" in Data or "who created you" in Data or "who brought you into existence" in Data or "who formed you" in Data or "who designed you" in Data or "who constructed you" in Data or "who gave you life" in Data or "who birthed you" in Data or "who manufactured you" in Data or "who engineered you" in Data or "who produced you" in Data:
            Speak("I have created by 19B Electronics Students of U.I.T under the supervision of Engineer Raza Jafri, My creators are Syed Muhammad Jari Abbas Rizvi,Saeed Bin Fareed, Syed Sharjeel Abbas Rizvi and Dheeraj Dhanji")
        elif "what is" in Data or "where is" in Data or"question" in Data or "answer" in Data:
            Reply = QuestionsAnswers(Data)
            Speak(Reply)
        
        elif "goodbye" in Data:
            pass    
            
        else:
            Reply=ReplyBrain(Data)
            Speak(Reply)

def wakedetected():
    query = WakeupDetected()
    if "True-Mic" in query:
        print("")
        print("Wakeup Detected")
        print("")
        MainExecution()
    


wakedetected()
