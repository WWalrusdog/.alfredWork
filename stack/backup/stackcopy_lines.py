#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
temp = open("/Users/scottmolloy/Desktop/.alfredWork/stack/temp.txt","r")
tempp = temp.read()
temp.close()
_delimeter = open("/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/delimeter.txt", "r")
delimeter = _delimeter.read().strip()
_delimeter.close()
temp = tempp
temp = "%%%"+temp
if delimeter == "\\n":
	delimeter = "\n"
temp = temp.replace(f"{delimeter}","%%%")
stack = open("/Users/scottmolloy/Desktop/.alfredWork/stack/stack.txt", "r")
old_stack = stack.read()
new_stack = temp+old_stack
if new_stack[-3:] == "%%%":
	new_stack = new_stack[:-3]
stack = open("stack.txt", "w")
stack.write(new_stack)
stack.close()