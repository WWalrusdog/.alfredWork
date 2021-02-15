#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip
from pynput.mouse import Button, Controller
mouse = Controller()
mouse.position = (474.0234375, 82.01171875)
mouse.press(Button.left)
mouse.release(Button.left)

