#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from pynput.keyboard import Key, Controller
keyboard = Controller()
import time
def check():
    file = open("ripcord.txt", "r")
    file.close()
keyboard.type("drawQuad")
keyboard.type("(")
with keyboard.pressed(Key.ctrl):
    keyboard.press("v")
    keyboard.release("v")
time.sleep(.5)
check()
with keyboard.pressed(Key.ctrl):
    keyboard.press("v")
    keyboard.release("v")
time.sleep(.5)
check()
with keyboard.pressed(Key.ctrl):
    keyboard.press("v")
    keyboard.release("v")
time.sleep(.5)
check()
with keyboard.pressed(Key.ctrl):
    keyboard.press("v")
    keyboard.release("v")
time.sleep(.3)
check()
time.sleep(.5)
check()
keyboard.type("newColor());")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(.1)
check()
