import time
import pyperclip
from pynput.keyboard import Key, Controller
keyboard = Controller()
from pynput.mouse import Button, Controller
mouse = Controller()
from playsound import playsound
def fixTuple(position):
    position = position.strip("(")
    position = position.strip(")")
    position = position.split(",")
    position[0] = float(position[0])
    position[1] = float(position[1])
    position = tuple(position)
    return(position)
def ding():
    playsound("clicksound.mp3")
    def click():
        mouse.press(Button.left)
        mouse.release(Button.left)
def record(num):
    coords = ""
    for i in range(num):
        time.sleep(3)
        ding()
        coords = coords+str(mouse.position)+"%%%"
        ding()
    file = open("executeRecorded.py", "w")
    file.write(f"""import time
from pynput.mouse import Button, Controller
mouse = Controller()
def click():
    mouse.press(Button.left)
    mouse.release(Button.left)
def fixTuple(position):
    position = position.strip("(")
    position = position.strip(")")
    position = position.split(",")
    position[0] = float(position[0])
    position[1] = float(position[1])
    position = tuple(position)
    return(position)
file = open("coords.txt", "r")
recorded = file.read()
file.close()
recorded = recorded.split("%%%")
prev = False
for i in range({num}):
    prev = mouse.position
    time.sleep(.3)
    x = fixTuple(recorded[i])
    if x == prev:
        time.sleep(1)
    else:
        mouse.position = x
        time.sleep(.1)
        click()""")
    file.close()
    file = open("coords.txt", 'w')
    file.write(coords)
    file.close()
    return coords

items = pyperclip.paste()
items = int(items)
record(items)