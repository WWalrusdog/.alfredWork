#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip as p
file = open("/Users/scottmolloy/Desktop/.alfredWork/stack/stack.txt", "r")
temp = file.read()
file.close()
temp = temp.replace("%%%", "\n")
p.copy(temp)
file = open("/Users/scottmolloy/Desktop/.alfredWork/stack/stack.txt", "w")
file.close()