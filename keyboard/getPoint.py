#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip
from pynput.mouse import Button, Controller
mouse = Controller()
x = mouse.position
pyperclip.copy(f"mouse.position = {x}")