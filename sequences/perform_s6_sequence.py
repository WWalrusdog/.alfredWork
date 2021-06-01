#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from pynput.keyboard import Key, Controller
keyboard = Controller()
import time
def check():
    file = open("ripcord.txt", "r")
    file.close()
with keyboard.pressed(Key.cmd):
    with keyboard.pressed(Key.alt):
        keyboard.press(Key.left)
        keyboard.release(Key.left)
time.sleep(.3)
check()
