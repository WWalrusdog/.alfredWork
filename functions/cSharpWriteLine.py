#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip as p
coverBases = p.paste().replace("\"", "\\\"")
p.copy(f"Console.WriteLine(\"{coverBases}\")")