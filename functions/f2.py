#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip as p
p.copy("<h2>"+"</h2><br>\n<h2>".join(p.paste().split("\n"))+"</h2>")