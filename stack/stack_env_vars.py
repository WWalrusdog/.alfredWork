#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
stack = open("/Users/scottmolloy/Desktop/.alfredWork/stack/stack.txt", "r").read().split("\t\t∴\n")
try:
    stack = stack[:len(stack)-1]
except:
    print("okay")
counter = len(stack)    
if counter > 0:
    next_item = stack[0]
else:
    next_item = "<empty>"
open("/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/sc.txt", "w").write(str(counter))
open("/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/sh.txt", "w").write(next_item)