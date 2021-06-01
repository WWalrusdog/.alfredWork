#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from pynput.keyboard import Key, Controller
keyboard = Controller()
import time
def check():
    file = open("ripcord.txt", "r")
    file.close()
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(.03)
check()
keyboard.press(Key.left)
keyboard.release(Key.left)
time.sleep(.03)
check()
with keyboard.pressed(Key.alt):
    with keyboard.pressed(Key.shift):
        keyboard.press(Key.right)
        keyboard.release(Key.right)
time.sleep(.1)
check()
with keyboard.pressed(Key.shift):
    keyboard.press(Key.right)
    keyboard.release(Key.right)
time.sleep(.1)
check()
keyboard.press(Key.delete)
keyboard.release(Key.delete)
time.sleep(.03)
check()
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(.03)
check()
keyboard.press(Key.down)
keyboard.release(Key.down)
time.sleep(.03)
check()
