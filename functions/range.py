#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip as p
content = open("/Users/scottmolloy/Desktop/.alfredWork/functions/previous_clip.txt", "r").read()
num = int(content)
content = ""
for i in range(num+1):
    content = content+str(i)+" "	
p.copy(content)