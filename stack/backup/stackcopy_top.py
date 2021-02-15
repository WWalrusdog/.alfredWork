#!/usr/bin/python
temp = open("temp.txt","r")
tempp = temp.read()
temp.close()
temp = tempp
temp = "%%%"+temp
stack = open("stack.txt", "r")
old_stack = stack.read()
new_stack = temp+old_stack
print(new_stack)
stack = open("stack.txt", "w")
stack.write(new_stack)
stack.close()
counter = open("stackcounter.txt", "r")
num = counter.read()
num = int(num)
num = num + 1
counter.close()
counter = open("stackcounter.txt", "w")
counter.write(num)
counter.close()