#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip as p
open("/Users/scottmolloy/Desktop/.alfredWork/functions/previous_clip.txt", "w").write(p.paste())