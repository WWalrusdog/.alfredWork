#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from pynput.keyboard import Key, Controller
keyboard = Controller()
import time
with keyboard.pressed(Key.cmd):
    keyboard.press(Key.right)
    keyboard.release(Key.right)
time.sleep(.05)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(.025)
keyboard.type("<li>")
