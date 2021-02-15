#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip as p
params = open("/Users/scottmolloy/Desktop/.alfredWork/functions/params.txt", "r").readlines()

p.copy( (int(params[1].strip()) * (str(params[0]))).strip())