#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip as p
prev_clip = open("/Users/scottmolloy/Desktop/.alfredWork/functions/previous_clip.txt", "r")
content = prev_clip.read()

content = content.replace(" ", """
""")

p.copy(content)