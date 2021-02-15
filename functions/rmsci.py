#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip as p
prev_clip = open("/Users/scottmolloy/Desktop/.alfredWork/functions/previous_clip.txt", "r")
content = prev_clip.read()
prev_clip.close()
def negativeScientific(item):
    if "E-" in item and "." in item:
        convert = item.split("E-")
        term = convert[0].replace(".", "")
        power = int(convert[1])
        out = "0." + (power-1)*"0"+term
        return(out)
content = content.replace("\n", "\t🐣")
content = content.split()
for i in range(len(content)):
    replace = negativeScientific(content[i])
    if replace:
        content[i] = replace
content = ("\t".join(content)).replace("🐣", "\n")
p.copy(content)