#!/usr/bin/python
temp = open("temp.txt","r")
tempp = temp.read()
temp.close()
temp = tempp
temp = "%%%"+temp
stack = open("stack.txt", "a+")
stack.write(temp)
print(temp)
