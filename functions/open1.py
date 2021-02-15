#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import os
params = open("/Users/scottmolloy/Desktop/.alfredWork/functions/params.txt", "r").read()
os.system(f"/Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl /Users/scottmolloy/Desktop/.alfredWork/FreeVariables/{params}.txt")