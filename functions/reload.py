#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from pynput.keyboard import Key, Controller
keyboard = Controller()
import time
with keyboard.pressed(Key.cmd):
    keyboard.press("l")
    keyboard.release("l")
time.sleep(.3)
with keyboard.pressed(Key.cmd):
    keyboard.press("v")
    keyboard.release("v")
time.sleep(.3)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(.1)
