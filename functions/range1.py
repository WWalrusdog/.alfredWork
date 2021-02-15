#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip as p
params = int(open("/Users/scottmolloy/Desktop/.alfredWork/functions/params.txt", "r").read())
content = ""
for i in range(params+1):
    content = content+str(i)+"\n"	
p.copy(content.strip())