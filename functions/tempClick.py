#!/usr/bin/python
from pynput.mouse import Button, Controller 
mouse = Controller()

returnM = mouse.position

mouse.position = (1262.11328125, 199.91015625)
time.sleep(.1)
mouse.press(Button.left)
mouse.release(Button.left)




mouse.position = (1368.0078125, 301.609375)
time.sleep(.1)
mouse.press(Button.left)
mouse.release(Button.left)
mouse.position = returnM