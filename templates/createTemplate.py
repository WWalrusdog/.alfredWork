#!/usr/bin/python
_in = open("temp.txt", "r")
whole = _in.read()
_in.close()
whole = whole.rstrip()
i = 0
_whole = ""
for char in whole:
    if char == "=" and i==0:
        i = 1
        _whole = _whole+"&&&"
    _whole = _whole+char
whole = _whole
outtemp = open("temp.txt", "w")
outtemp.write(whole)
outtemp.close()
_in = open("temp.txt", "r")
whole = _in.read()
whole = whole.rstrip()
whole.rstrip("\"")
_in.close()
parsed = whole.split("&&&=")
var_name = parsed[0]
var_data = parsed[1]
var_data = var_data.lstrip(" ")
var_name = var_name.rstrip(" ")+".txt"
out = open(var_name, "w")
out.write(var_data)
out.close()