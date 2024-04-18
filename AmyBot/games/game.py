from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import random

def stgame():
    chrome_options = Options()
    chrome_options.add_argument("--kiosk")

    driver = webdriver.Chrome(options=chrome_options)
    games = [
        "file:///home/teamelectro/FYP/TemplateForJarvis/games/MathGame/index.html" , 
        "file:///home/teamelectro/FYP/TemplateForJarvis/games/Menja/index.html" , 
        "file:///home/teamelectro/FYP/TemplateForJarvis/games/memory-game/index.html"]
    g_choice = random.choice(games)
    driver.get(g_choice)
    time.sleep(15)
    # Close the browser
    driver.quit()
    # webbrowser.open(g_choice)

# stgame()

def sgame(path):
    chrome_options = Options()
    chrome_options.add_argument("--kiosk")

    driver = webdriver.Chrome(options=chrome_options)
    game = path
    driver.get(game)
    time.sleep(50)
    # Close the browser
    driver.quit()


# sgame("file:///home/teamelectro/FYP/TemplateForJarvis/games/MathGame/index.html")