#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from pynput.keyboard import Key, Controller
keyboard = Controller()
import time
def check():
    file = open("ripcord.txt", "r")
    file.close()
with keyboard.pressed(Key.cmd):
    keyboard.press("a")
    keyboard.release("a")
time.sleep(.3)
check()
time.sleep(.5)
check()
with keyboard.pressed(Key.ctrl):
    keyboard.press("c")
    keyboard.release("c")
time.sleep(.3)
check()
time.sleep(.5)
check()
exec(open('/Users/scottmolloy/Desktop/.alfredWork/sequences/perform_s8_sequence.py').read())
