#!/usr/bin/python
_stack = open("stack.txt", "r")
stack = _stack.read()
_stack.close()
stack = stack.split("%%%")
stack = stack[1:]
pop_index = len(stack)-1
if len(stack) == 0:
    pop = "<empty>"
else:
    pop = stack[pop_index].strip("\n")
    stack = stack[:pop_index]
    print(pop)
    remake_stack = ""
    for i in range(0, len(stack)):
        remake_stack = remake_stack+"%%%"+stack[i].rstrip("\n")
    _stack = open("stack.txt", "w")
    _stack.write(remake_stack)
    _stack.close()
out = open("out.txt", "w")
out.write(pop)
out.close()
counter = open("stackcounter.txt", "r")
num = counter.read()
num = int(num)
num = num + 1
counter.close()
report = open("stackcounter.txt", "w")
report.write(num)
report.close()