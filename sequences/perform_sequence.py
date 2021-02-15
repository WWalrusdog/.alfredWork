#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from pynput.keyboard import Key, Controller
keyboard = Controller()
import time
keyboard.press(Key.tab)
keyboard.release(Key.tab)
time.sleep(.2)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
time.sleep(.2)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
time.sleep(.2)
