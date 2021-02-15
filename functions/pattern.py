#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip as p
import re
prev_clip = open("/Users/scottmolloy/Desktop/.alfredWork/functions/previous_clip.txt", "r")
content = prev_clip.read()
prev_clip.close()

_pattern = open("/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/pattern.txt", "r")
pattern = _pattern.read()
_pattern.close()


p.copy("\n".join(re.findall(pattern, content)))