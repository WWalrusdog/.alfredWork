#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip
from pynput.mouse import Button, Controller
mouse = Controller()
x = mouse.position
x = list(x)
x[1] = x[1]+100
mouse.position = x