#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from pynput.keyboard import Key, Controller
keyboard = Controller()
import time
def check():
    file = open("ripcord.txt", "r")
    file.close()
with keyboard.pressed(Key.cmd):
    keyboard.press("f")
    keyboard.release("f")
time.sleep(.3)
check()
keyboard.type("https://serve.castfire.com")
keyboard.press(Key.esc)
keyboard.release(Key.esc)
time.sleep(.1)
check()
