#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip
from pynput.mouse import Button, Controller
mouse = Controller()
from pynput.keyboard import Key, Controller
keyboard = Controller()
def circle():
	mouse.position = (666.0390625, 637.59765625)

	x = mouse.position
	x = list(x)
	x[0] = x[0]-40
	mouse.position = x

	mouse.press(Button.left)
	mouse.release(Button.left)

	keyboard.type("d")
	time.sleep(.2)
	keyboard.type("d")
	time.sleep(.2)
	keyboard.type("d")
	time.sleep(5)

	x = mouse.position
	x = list(x)
	x[1] = x[1]-40
	mouse.position = x

	mouse.press(Button.left)
	mouse.release(Button.left)

	keyboard.type("d")
	time.sleep(.2)
	keyboard.type("d")
	time.sleep(.2)
	keyboard.type("d")
	time.sleep(5)


	x = mouse.position
	x = list(x)
	x[0] = x[0]+40
	mouse.position = x

	mouse.press(Button.left)
	mouse.release(Button.left)

	keyboard.type("d")
	time.sleep(.2)
	keyboard.type("d")
	time.sleep(.2)
	keyboard.type("d")
	time.sleep(5)


	x = mouse.position
	x = list(x)
	x[1] = x[1]+40
	mouse.position = x

	mouse.press(Button.left)
	mouse.release(Button.left)

	keyboard.type("d")
	time.sleep(.2)
	keyboard.type("d")
	time.sleep(.2)
	keyboard.type("d")
	time.sleep(5)



circle()


