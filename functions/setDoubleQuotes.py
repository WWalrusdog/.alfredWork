#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from pynput.keyboard import Key, Controller
keyboard = Controller()
import time
def check():
    file = open("ripcord.txt", "r")
    file.close()
keyboard.type("\"")
keyboard.type("\"")
keyboard.press(Key.left)
keyboard.release(Key.left)
time.sleep(.1)
check()
