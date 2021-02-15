#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip
from pynput.mouse import Button, Controller
mouse = Controller()
from pynput.keyboard import Key, Controller
keyboard = Controller()

for i in range(800):
	exec(open('/Users/scottmolloy/Desktop/.alfredWork/functions/mine.py').read())
