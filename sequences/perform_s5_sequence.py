#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from pynput.keyboard import Key, Controller
keyboard = Controller()
import time
def check():
    file = open("ripcord.txt", "r")
    file.close()
with keyboard.pressed(Key.cmd):
    with keyboard.pressed(Key.alt):
        keyboard.press(Key.right)
        keyboard.release(Key.right)
time.sleep(.3)
check()
with keyboard.pressed(Key.cmd):
    with keyboard.pressed(Key.alt):
        keyboard.press(Key.right)
        keyboard.release(Key.right)
time.sleep(.3)
check()
with keyboard.pressed(Key.cmd):
    with keyboard.pressed(Key.alt):
        keyboard.press(Key.right)
        keyboard.release(Key.right)
time.sleep(.3)
check()
with keyboard.pressed(Key.cmd):
    with keyboard.pressed(Key.alt):
        keyboard.press(Key.right)
        keyboard.release(Key.right)
time.sleep(.3)
check()
with keyboard.pressed(Key.cmd):
    with keyboard.pressed(Key.alt):
        keyboard.press(Key.right)
        keyboard.release(Key.right)
time.sleep(.3)
check()
