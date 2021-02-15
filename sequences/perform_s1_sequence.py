#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from pynput.keyboard import Key, Controller
keyboard = Controller()
import time
def check():
    file = open("ripcord.txt", "r")
    file.close()
keyboard.type("quick")
keyboard.type("actions")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(.1)
check()
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(.1)
check()
