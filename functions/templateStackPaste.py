#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip as p
def stackTemplated():
    stack = open("/Users/scottmolloy/Desktop/.alfredWork/stack/stack.txt", "r").read().split("\t\t∴\n")
    form = open("/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/states/form.txt", "r").read()
    paste = ""
    for i in range(len(stack)):
        paste = paste+form.replace("{sh}",stack[i])+"\n"
    open("/Users/scottmolloy/Desktop/.alfredWork/stack/stack.txt", "w").write("")
    if paste:
        return(paste)
    else:
        return(form)

p.copy(stackTemplated())