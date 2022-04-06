import pyautogui as auto
import random
import time
import requests
keys = (' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', 'enter', '?', '@', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~')

auto.FAILSAFE = True
auto.PAUSE = 0.001
# time.sleep(2)
def random_keyPress():
    # auto.press(keys[random.randint(0, 69)])
    auto.press(keys[random.randint(0, len(keys) - 1)])
def FML():
    y = 0
    while True:
        # time.sleep(0.1)
    
        x = random.randint(1, 8)
        # x = 7
        if x == 1:
            random_keyPress()
        if x == 2:
            auto.moveTo(random.randint(0, 1920), random.randint(0, 1080))
        if x == 3:
            auto.dragTo(random.randint(0, 1920), random.randint(0, 1080))
        if x == 4:
            auto.click()
        if x == 5:
            req = requests.get("https://random-word-api.herokuapp.com/word?number=1")
            text = req.json()[0]
            auto.write(text)
        if x == 6:
            auto.scroll(random.randint(-10, 10))
        if x == 7:
            auto.press('enter')
        y = y + 1
FML()
