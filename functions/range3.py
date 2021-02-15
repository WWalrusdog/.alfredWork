#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip as p
params = open("/Users/scottmolloy/Desktop/.alfredWork/functions/params.txt", "r").readlines()
content = ""
if(float(params[2])%1 == 0):
	i = int(params[0].strip())
	while(i <=  int(params[1].strip())+int(params[2])):
	    content = content+str(i)+"\n"
	    i+=int(params[2])
	
else:
	i = float(params[0].strip())
	while(i <  float(params[1].strip())+float(params[2])):
	    content = content+str(i)+"\n"
	    i+=float(params[2])

p.copy(content.strip())