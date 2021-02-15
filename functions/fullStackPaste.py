#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip as p
def fullStackPaste():
	stack = open("/Users/scottmolloy/Desktop/.alfredWork/stack/stack.txt", "r").read().split("\t\t∴\n")
	paste = ""
	for i in range(len(stack)):
	    paste = paste + "\n" + stack[i]
	open("/Users/scottmolloy/Desktop/.alfredWork/stack/stack.txt", "w").write("")
	paste = paste.strip("\n")
	if paste:
	    return(paste)
	else:
	    return("<empty>")

p.copy(fullStackPaste())