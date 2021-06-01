#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from pynput.keyboard import Key, Controller
keyboard = Controller()
import time
def check():
    file = open("ripcord.txt", "r")
    file.close()
with keyboard.pressed(Key.cmd):
    keyboard.press("l")
    keyboard.release("l")
time.sleep(1)
check()
keyboard.press(Key.left)
keyboard.release(Key.left)
time.sleep(.05)
check()
keyboard.type("view-source:")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(.05)
check()
with keyboard.pressed(Key.alt):
    with keyboard.pressed(Key.cmd):
        keyboard.press(Key.right)
        keyboard.release(Key.right)
time.sleep(.1)
check()
