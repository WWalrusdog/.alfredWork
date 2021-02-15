#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip as p
prev_clip = open("/Users/scottmolloy/Desktop/.alfredWork/functions/previous_clip.txt", "r")
content = prev_clip.read()
prev_clip.close()
out = open(f"{content}.py", "r")
function = out.read()
out.close()
out = open("f1.py", "w")
out.write(f"{function}")
out.close()