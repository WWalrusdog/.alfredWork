#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip
from pynput.mouse import Button, Controller
mouse = Controller()
x = mouse.position
x = list(x)
x[0] = x[0]-100
mouse.position = x