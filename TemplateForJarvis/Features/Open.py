import os
import keyboard
import pyautogui
import webbrowser
from time import sleep
import pygame
import random
pygame.init()

poems=[r"Poems/Baa-Baa-Black-Sheep-.mp3",r"Poems/WheelsOn-the-Bus.1.mp3","Poems\\twinkle-star.mp3"]
P_choice = random.choice(poems)


def OpenExe(Query):
    Query = str(Query).lower()
    
    if "visit" in Query:
        Nameofweb = Query.replace("visit ","")
        link = f"https://www.{Nameofweb}.com"
        webbrowser.open(link)
        return True
    
    elif "launch" in Query:
        Nameofweb = Query.replace("launch ","")
        link = f"https://www.{Nameofweb}.com"
        webbrowser.open(link)
        return True
    
    
    elif "open" in Query:
        Nameoftheapp = Query.replace("open ","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(Nameoftheapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)
        return True
    elif "start" in Query:
        Nameoftheapp = Query.replace("start ","")
        if "poem" in Nameoftheapp:
            pygame.mixer.music.load(P_choice)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        return True
    
    
    
        
        # pyautogui.press('win')
        # sleep(1)
        # keyboard.write(Nameoftheapp)
        # sleep(1)
        # keyboard.press('enter')
        # sleep(0.5)
        # return 
   