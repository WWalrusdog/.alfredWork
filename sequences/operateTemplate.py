#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import re

file_name = open("name_of_file.txt", "r")
filename = file_name.read()
filename = filename.rstrip(" ")
file_name.close()

file = open(filename+".txt", "r")
content = file.read()
file.close()

y = re.findall("\{[^{]*}", content)

for i in range(len(y)):
    var = (y[i].rstrip("}").lstrip("{")+".txt")
    _var = open(f"/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/{var}", "r")
    var = _var.read()
    _var.close()
    content = content.replace(y[i], var)

file = open("template_output.txt", "w")
file.write(content)
file.close()