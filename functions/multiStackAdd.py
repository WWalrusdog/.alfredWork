#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip as p
def stackAdd(content):
    stack = open("/Users/scottmolloy/Desktop/.alfredWork/stack/stack.txt", "r").read()
    outstack = f"{content}\t\t∴\n{stack}"
    open("/Users/scottmolloy/Desktop/.alfredWork/stack/stack.txt", "w").write(outstack)
def multiStackAdd(content):
    try:
        lim = open(f"/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/states/delimeter.txt", "r").read()
    except:
        lim = "\n"
    stackAdd(content.replace(lim,"\t\t∴\n"))

multiStackAdd(p.paste())