#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip as p
def reverseAdd(content):
    stack = open("/Users/scottmolloy/Desktop/.alfredWork/stack/stack.txt", "r").read()
    outstack = f"{stack}\t\t∴\n{content}"
    open("/Users/scottmolloy/Desktop/.alfredWork/stack/stack.txt", "w").write(outstack)

reverseAdd(p.paste())