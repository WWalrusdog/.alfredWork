#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip as p
content = open("/Users/scottmolloy/Desktop/.alfredWork/functions/previous_clip.txt", "r").read()
quantity = int(open("/Users/scottmolloy/Desktop/.alfredWork/functions/params.txt", "r").read().strip())

p.copy((quantity*content).strip())