#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip as p
params = open("/Users/scottmolloy/Desktop/.alfredWork/functions/params.txt", "r").readlines()
content = ""
i = int(params[0].strip())
while(i <  int(params[1].strip())+1):
    content = content+str(i)+"\n"
    i+=1
p.copy(content.strip())