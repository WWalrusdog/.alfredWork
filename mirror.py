#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip as p
temp = p.paste().split("\n")
out = ""
length = len(temp)-1
for i in range(length+1):
    temp[length-i] = temp[length-i].strip("\n")+"\n"
    out = out+temp[length-i]
p.copy(out)