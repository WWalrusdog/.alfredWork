#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
_temp = open("temp.txt", "r")
read_in = _temp.read()
_temp.close()
read_in = read_in.split("=")
title = read_in[0]
content = str(read_in[1:]).strip("['").strip("]").rstrip("\'").lstrip(" ")
print(title)
print(content)
title = title.rstrip(" ")
file = open("function.txt", "w")
file.write(content)
file.close()
file = open("title.txt", "w")
file.write(title)
file.close()