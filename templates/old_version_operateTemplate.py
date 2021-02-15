#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

file_name = open("name_of_file.txt", "r")
filename = file_name.read()
filename = filename.rstrip(" ")
file_name.close()

file = open(filename+".txt", "r")
content = file.read()
file.close()
if "{0}" in content:    
    _r0 = open("/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/r0.txt", "r")
    print("true")
    r0 = _r0.read()
    _r0.close()
    content = content.replace("{0}",r0)
if "{1}" in content:    
    _r1 = open("/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/r1.txt", "r")
    r1 = _r1.read()
    _r1.close()
    content = content.replace("{1}",r1)
if "{2}" in content:    
    _r2 = open("/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/r2.txt", "r")
    r2 = _r2.read()
    _r2.close()
    content = content.replace("{2}",r2)
if "{3}" in content:    
    _r3 = open("/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/r3.txt", "r")
    r3 = _r3.read()
    _r3.close()
    content = content.replace("{3}",r3)
if "{4}" in content:    
    _r4 = open("/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/r4.txt", "r")
    r4 = _r4.read()
    _r4.close()
    content = content.replace("{4}",r4)
if "{5}" in content:    
    _r5 = open("/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/r5.txt", "r")
    r5 = _r5.read()
    _r5.close()
    content = content.replace("{5}",r5)
if "{6}" in content:    
    _r6 = open("/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/r6.txt", "r")
    r6 = _r6.read()
    _r6.close()
    content = content.replace("{6}",r6)
if "{7}" in content:    
    _r7 = open("/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/r7.txt", "r")
    r7 = _r7.read()
    _r7.close()
    content = content.replace("{7}",r7)
if "{8}" in content:    
    _r8 = open("/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/r8.txt", "r")
    r8 = _r8.read()
    _r8.close()
    content = content.replace("{8}",r8)
if "{9}" in content:    
    _r9 = open("/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/r9.txt", "r")
    r9 = _r9.read()
    _r9.close()
    content = content.replace("{9}",r9)
file = open("template_output.txt", "w")
file.write(content)
file.close()