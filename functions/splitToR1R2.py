#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip as p
open("/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/r1.txt","w").write(p.paste().split(" ")[0].strip(" "))
open("/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/r2.txt","w").write(p.paste().split(" ")[1].strip(" "))