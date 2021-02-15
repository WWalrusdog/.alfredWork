mine = #!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip
from pynput.mouse import Button, Controller
mouse = Controller()
from pynput.keyboard import Key, Controller
keyboard = Controller()
def circle():
	

	x = mouse.position
	x = list(x)
	x[0] = x[0]-40
	mouse.position = x

	mouse.press(Button.left)
	mouse.release(Button.left)

	keyboard.type("d")
	time.sleep(.03)
	keyboard.type("d")
	time.sleep(5)


	x = mouse.position
	x = list(x)
	x[1] = x[1]-40
	mouse.position = x

	mouse.press(Button.left)
	mouse.release(Button.left)

	keyboard.type("d")
	time.sleep(.03)
	keyboard.type("d")
	time.sleep(5)


	x = mouse.position
	x = list(x)
	x[0] = x[0]+40

	

	time.sleep(.2)

	mouse.press(Button.left)
	mouse.release(Button.left)


	keyboard.type("d")
	time.sleep(.03)
	keyboard.type("d")
	time.sleep(5)

	mouse.position = x

	mouse.press(Button.left)
	mouse.release(Button.left)

	
	x = mouse.position
	x = list(x)
	x[1] = x[1]+40

	mouse.press(Button.left)
	mouse.release(Button.left)

	time.sleep(.2)
	keyboard.type("d")
	time.sleep(.03)
	keyboard.type("d")
	time.sleep(5)


circle()


