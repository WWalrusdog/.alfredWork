#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from pynput.keyboard import Key, Controller
keyboard = Controller()
import time
def check():
    file = open("ripcord.txt", "r")
    file.close()
exec(open('/Users/scottmolloy/Desktop/.alfredWork/sequences/perform_s0_sequence.py').read())
