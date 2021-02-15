#!/usr/bin/python
from pynput.mouse import Button, Controller 
mouse = Controller()
mouse.press(Button.left)
mouse.release(Button.left)