#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip as p
p.copy("<h3>"+"</h3><br>\n<h3>".join(p.paste().split("\n"))+"</h3>")