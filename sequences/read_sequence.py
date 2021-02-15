#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip as p
file = open("/Users/scottmolloy/Desktop/.alfredWork/sequences/name_of_file.txt", "r")
name = file.read()
file.close()
name = name.strip(" ")
file = open(f"/Users/scottmolloy/Desktop/.alfredWork/sequences/{name}.txt", "r")
content = file.read()
file.close()
p.copy(content)