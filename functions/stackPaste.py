#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip as p
def stackPaste():
    stack = open("/Users/scottmolloy/Desktop/.alfredWork/stack/stack.txt", "r").read().split("\t\t∴\n")
    outstack = "\t\t∴\n".join(stack[1:])
    paste = stack[0]
    open("/Users/scottmolloy/Desktop/.alfredWork/stack/stack.txt", "w").write(outstack)
    if paste:
        return(paste)
    else:
        return("<empty>")

p.copy(stackPaste())