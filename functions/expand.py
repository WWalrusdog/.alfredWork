#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip as p
prev_clip = open("/Users/scottmolloy/Desktop/.alfredWork/functions/previous_clip.txt", "r")
content = prev_clip.read()

file = open(f"/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/states/count.txt", "r").read()
quantity = int(file.strip(" ")) 

p.copy(quantity*content)	