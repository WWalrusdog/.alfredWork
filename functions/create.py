#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip as p
prev_clip = open("/Users/scottmolloy/Desktop/.alfredWork/functions/previous_clip.txt", "r")
content = prev_clip.read()
prev_clip.close()
source = content.split(":")[1][1:]
destination_name = content.split(":")[0]
guide = source.split("replace")[1]
term1 = guide.split(",")[0][1:]
term2 = guide.split(",")[1][1:-1]
script = f"""#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip as p
prev_clip = open("/Users/scottmolloy/Desktop/.alfredWork/functions/previous_clip.txt", "r")
content = prev_clip.read()
prev_clip.close()
content = content.replace("{term1}", "{term2}")
p.copy(content)"""

out = open(f"/Users/scottmolloy/Desktop/.alfredWork/functions/{destination_name}.py", "w")
out.write(script)
out.close()