#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip as p
def stackAdd(content):
    stack = open("/Users/scottmolloy/Desktop/.alfredWork/stack/stack.txt", "r").read()
    outstack = f"{content}\t\t∴\n{stack}"
    open("/Users/scottmolloy/Desktop/.alfredWork/stack/stack.txt", "w").write(outstack)

stackAdd(p.paste())