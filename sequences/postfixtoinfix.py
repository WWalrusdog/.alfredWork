#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from pynput.keyboard import Key, Controller
keyboard = Controller()
import time
import pyperclip as p
for i in range(19):
    with keyboard.pressed(Key.cmd):
        keyboard.press("c")
        keyboard.release("c")
    time.sleep(.5)
    if p.paste() == "*":
        with keyboard.pressed(Key.alt):
            with keyboard.pressed(Key.ctrl):
                keyboard.press("c")
                keyboard.release("c")
        time.sleep(.5)
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        with keyboard.pressed(Key.ctrl):
            keyboard.press("c")
            keyboard.release("c")
        time.sleep(.5)
        keyboard.press(Key.up)
        keyboard.release(Key.up)
        time.sleep(.3)
        with keyboard.pressed(Key.alt):
            with keyboard.pressed(Key.ctrl):
                keyboard.press("c")
                keyboard.release("c")
        time.sleep(.5)
        keyboard.press(Key.right)
        keyboard.release(Key.right)
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        keyboard.press(Key.delete)
        keyboard.release(Key.delete)
        time.sleep(.2)
        keyboard.press(Key.f2)
        keyboard.release(Key.f2)
        time.sleep(.5)
        with keyboard.pressed(Key.ctrl):
            keyboard.press("v")
            keyboard.release("v")
        time.sleep(.3)
        time.sleep(.5)
        with keyboard.pressed(Key.ctrl):
            keyboard.press("v")
            keyboard.release("v")
        time.sleep(.3)
        time.sleep(.5)
        with keyboard.pressed(Key.ctrl):
            keyboard.press("v")
            keyboard.release("v")
        time.sleep(.3)
        time.sleep(.5)
        with keyboard.pressed(Key.shift):
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
        time.sleep(.3)
        with keyboard.pressed(Key.shift):
            keyboard.press(Key.up)
            keyboard.release(Key.up)
        time.sleep(.3)
        with keyboard.pressed(Key.shift):
            with keyboard.pressed(Key.cmd):
                keyboard.press(Key.right)
                keyboard.release(Key.right)
        time.sleep(.8)
        with keyboard.pressed(Key.ctrl):
            keyboard.press("d")
            keyboard.release("d")
        time.sleep(.3)
        time.sleep(.5)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(.3)
        keyboard.press(Key.up)
        keyboard.release(Key.up)
        time.sleep(.3)
        with keyboard.pressed(Key.cmd):
            keyboard.press("c")
            keyboard.release("c")
        time.sleep(.5)
        with keyboard.pressed(Key.shift):
            with keyboard.pressed(Key.cmd):
                keyboard.press(Key.right)
                keyboard.release(Key.right)
        time.sleep(.3)
        with keyboard.pressed(Key.cmd):
            keyboard.press("v")
            keyboard.release("v")
        time.sleep(.5)
        keyboard.press(Key.up)
        keyboard.release(Key.up)
    elif p.paste() == "/":
        with keyboard.pressed(Key.alt):
            with keyboard.pressed(Key.ctrl):
                keyboard.press("c")
                keyboard.release("c")
        time.sleep(.5)
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        with keyboard.pressed(Key.ctrl):
            keyboard.press("c")
            keyboard.release("c")
        time.sleep(.5)
        keyboard.press(Key.up)
        keyboard.release(Key.up)
        time.sleep(.3)
        with keyboard.pressed(Key.alt):
            with keyboard.pressed(Key.ctrl):
                keyboard.press("c")
                keyboard.release("c")
        time.sleep(.5)
        keyboard.press(Key.right)
        keyboard.release(Key.right)
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        keyboard.press(Key.delete)
        keyboard.release(Key.delete)
        time.sleep(.2)
        keyboard.press(Key.f2)
        keyboard.release(Key.f2)
        time.sleep(.5)
        with keyboard.pressed(Key.ctrl):
            keyboard.press("v")
            keyboard.release("v")
        time.sleep(.3)
        time.sleep(.5)
        with keyboard.pressed(Key.ctrl):
            keyboard.press("v")
            keyboard.release("v")
        time.sleep(.3)
        time.sleep(.5)
        with keyboard.pressed(Key.ctrl):
            keyboard.press("v")
            keyboard.release("v")
        time.sleep(.3)
        time.sleep(.5)
        with keyboard.pressed(Key.shift):
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
        time.sleep(.3)
        with keyboard.pressed(Key.shift):
            keyboard.press(Key.up)
            keyboard.release(Key.up)
        time.sleep(.3)
        with keyboard.pressed(Key.shift):
            with keyboard.pressed(Key.cmd):
                keyboard.press(Key.right)
                keyboard.release(Key.right)
        time.sleep(.8)
        with keyboard.pressed(Key.ctrl):
            keyboard.press("d")
            keyboard.release("d")
        time.sleep(.3)
        time.sleep(.5)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(.3)
        keyboard.press(Key.up)
        keyboard.release(Key.up)
        time.sleep(.3)
        with keyboard.pressed(Key.cmd):
            keyboard.press("c")
            keyboard.release("c")
        time.sleep(.5)
        with keyboard.pressed(Key.shift):
            with keyboard.pressed(Key.cmd):
                keyboard.press(Key.right)
                keyboard.release(Key.right)
        time.sleep(.3)
        with keyboard.pressed(Key.cmd):
            keyboard.press("v")
            keyboard.release("v")
        time.sleep(.5)
        keyboard.press(Key.up)
        keyboard.release(Key.up)
    elif p.paste() == "-":
        with keyboard.pressed(Key.alt):
            with keyboard.pressed(Key.ctrl):
                keyboard.press("c")
                keyboard.release("c")
        time.sleep(.5)
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        with keyboard.pressed(Key.ctrl):
            keyboard.press("c")
            keyboard.release("c")
        time.sleep(.5)
        keyboard.press(Key.up)
        keyboard.release(Key.up)
        time.sleep(.3)
        with keyboard.pressed(Key.alt):
            with keyboard.pressed(Key.ctrl):
                keyboard.press("c")
                keyboard.release("c")
        time.sleep(.5)
        keyboard.press(Key.right)
        keyboard.release(Key.right)
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        keyboard.press(Key.delete)
        keyboard.release(Key.delete)
        time.sleep(.2)
        keyboard.press(Key.f2)
        keyboard.release(Key.f2)
        time.sleep(.5)
        keyboard.press("(")
        keyboard.release("(")
        with keyboard.pressed(Key.ctrl):
            keyboard.press("v")
            keyboard.release("v")
        time.sleep(.3)
        time.sleep(.5)    
        keyboard.press(")")
        keyboard.release(")")
        with keyboard.pressed(Key.ctrl):
            keyboard.press("v")
            keyboard.release("v")
        time.sleep(.3)
        time.sleep(.5)
        keyboard.press("(")
        keyboard.release("(")
        with keyboard.pressed(Key.ctrl):
            keyboard.press("v")
            keyboard.release("v")
        time.sleep(.3)
        time.sleep(.5)
        keyboard.press(")")
        keyboard.release(")")
        with keyboard.pressed(Key.shift):
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
        time.sleep(.3)
        with keyboard.pressed(Key.shift):
            keyboard.press(Key.up)
            keyboard.release(Key.up)
        time.sleep(.3)
        with keyboard.pressed(Key.shift):
            with keyboard.pressed(Key.cmd):
                keyboard.press(Key.right)
                keyboard.release(Key.right)
        time.sleep(.8)
        with keyboard.pressed(Key.ctrl):
            keyboard.press("d")
            keyboard.release("d")
        time.sleep(.3)
        time.sleep(.5)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(.3)
        keyboard.press(Key.up)
        keyboard.release(Key.up)
        time.sleep(.3)
        with keyboard.pressed(Key.cmd):
            keyboard.press("c")
            keyboard.release("c")
        time.sleep(.5)
        with keyboard.pressed(Key.shift):
            with keyboard.pressed(Key.cmd):
                keyboard.press(Key.right)
                keyboard.release(Key.right)
        time.sleep(.3)
        with keyboard.pressed(Key.cmd):
            keyboard.press("v")
            keyboard.release("v")
        time.sleep(.5)
        keyboard.press(Key.up)
        keyboard.release(Key.up)
    elif p.paste() == "+":
        with keyboard.pressed(Key.alt):
            with keyboard.pressed(Key.ctrl):
                keyboard.press("c")
                keyboard.release("c")
        time.sleep(.5)
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        with keyboard.pressed(Key.ctrl):
            keyboard.press("c")
            keyboard.release("c")
        time.sleep(.5)
        keyboard.press(Key.up)
        keyboard.release(Key.up)
        time.sleep(.3)
        with keyboard.pressed(Key.alt):
            with keyboard.pressed(Key.ctrl):
                keyboard.press("c")
                keyboard.release("c")
        time.sleep(.5)
        keyboard.press(Key.right)
        keyboard.release(Key.right)
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        keyboard.press(Key.delete)
        keyboard.release(Key.delete)
        time.sleep(.2)
        keyboard.press(Key.f2)
        keyboard.release(Key.f2)
        time.sleep(.5)
        keyboard.press("(")
        keyboard.release("(")
        with keyboard.pressed(Key.ctrl):
            keyboard.press("v")
            keyboard.release("v")
        time.sleep(.3)
        time.sleep(.5)
        keyboard.press(")")
        keyboard.release(")")
        with keyboard.pressed(Key.ctrl):
            keyboard.press("v")
            keyboard.release("v")
        time.sleep(.3)
        time.sleep(.5)
        keyboard.press("(")
        keyboard.release("(")
        with keyboard.pressed(Key.ctrl):
            keyboard.press("v")
            keyboard.release("v")
        time.sleep(.3)
        time.sleep(.5)
        keyboard.press(")")
        keyboard.release(")")
        with keyboard.pressed(Key.shift):
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
        time.sleep(.3)
        with keyboard.pressed(Key.shift):
            keyboard.press(Key.up)
            keyboard.release(Key.up)
        time.sleep(.3)
        with keyboard.pressed(Key.shift):
            with keyboard.pressed(Key.cmd):
                keyboard.press(Key.right)
                keyboard.release(Key.right)
        time.sleep(.8)
        with keyboard.pressed(Key.ctrl):
            keyboard.press("d")
            keyboard.release("d")
        time.sleep(.3)
        time.sleep(.5)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(.3)
        keyboard.press(Key.up)
        keyboard.release(Key.up)
        time.sleep(.3)
        with keyboard.pressed(Key.cmd):
            keyboard.press("c")
            keyboard.release("c")
        time.sleep(.5)
        with keyboard.pressed(Key.shift):
            with keyboard.pressed(Key.cmd):
                keyboard.press(Key.right)
                keyboard.release(Key.right)
        time.sleep(.3)
        with keyboard.pressed(Key.cmd):
            keyboard.press("v")
            keyboard.release("v")
        time.sleep(.5)
        keyboard.press(Key.up)
        keyboard.release(Key.up)
    else:
        keyboard.press(Key.right)
        keyboard.release(Key.right)
        keyboard.press(Key.up)
        keyboard.release(Key.up)    
