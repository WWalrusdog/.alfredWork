#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip as p
content = open("/Users/scottmolloy/.pocketdimension/c#temp.txt").read()
if not content:
    content = p.paste()
p.copy(content)

