#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
op = open("/Users/scottmolloy/Desktop/.alfredWork/functions/file_name.txt", "r")
info = op.read().strip()
op.close()

if("(" in info):
    title = info.split("(")[0]
    options = info.split("(")[1].rstrip(")")
    if(len(options)>0):
        title += str(len(options.split(",")))
        options = options.split(",")
        open("/Users/scottmolloy/Desktop/.alfredWork/functions/params.txt", "w").write("\n".join(options))
else:
    title = info





file = open("/Users/scottmolloy/Desktop/.alfredWork/functions/operate.sh", "w")

file.write(f"""#!/bin/bash
chmod 755 /Users/scottmolloy/Desktop/.alfredWork/functions/{title}.py
/Users/scottmolloy/Desktop/.alfredWork/functions/{title}.py""")
file.close()