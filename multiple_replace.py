#!/usr/bin/python
_form = open("form.txt", "r")
form = _form.read()
sets = form.split(",,")
num_sets = len(sets)
start_values = open("start_values.txt", "w")
end_values = open("end_values.txt", "w")
for i in range(num_sets):
    seti = sets[i]
    seti = seti.split("::")
    start_values.write(seti[0]+"%%%")
    end_values.write(seti[1]+"%%%")
end_values.close()
start_values.close()
infile = open("start_values.txt", "r")
start_values = infile.read()
infile.close()
start_values = start_values.strip(" ")
start_values = start_values.strip("%%%")
start_values = start_values.split("%%%")
number_of_start_values = len(start_values)
infile = open("end_values.txt", "r")
end_values = infile.read()
infile.close()
end_values = end_values.strip(" ")
end_values = end_values.strip("%%%")
end_values = end_values.split("%%%")
number_of_end_values = len(end_values)
infile = open("template.txt", "r")
template = infile.read()
infile.close()
flag = 0
for item in end_values:
    if item in start_values:
        flag = 1
        print("1")
if number_of_end_values != number_of_start_values:
    flag = 1
    print("2")
if flag == 1:
    print("error")
else:
    for i in range(number_of_end_values):
        template = template.replace(start_values[i], end_values[i])
out = open("out.txt", 'w')
out.write(template)
out.close()
