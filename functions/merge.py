#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip
from pynput.mouse import Button, Controller
import time
mouse = Controller()
mouse.position = (604.765625, 116.9296875)
time.sleep(.3)

mouse.press(Button.left)
mouse.release(Button.left)
time.sleep(.3)
mouse.position = (195.48828125, 177.76953125)
time.sleep(.3)
mouse.press(Button.left)
mouse.release(Button.left)