import time
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
for i in range(2):
    prev = mouse.position
    time.sleep(.3)
    x = fixTuple(recorded[i])
    if x == prev:
        time.sleep(1)
    else:
        mouse.position = x
        time.sleep(.1)
        click()