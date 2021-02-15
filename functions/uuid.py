#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip as p
# Printing random id using uuid1() 
import uuid 
p.copy(str(uuid.uuid1())) 