#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip
from pynput.mouse import Button, Controller
mouse = Controller()
mouse.position = (316.2265625, 83.8984375)
mouse.press(Button.left)
mouse.release(Button.left)

