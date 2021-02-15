#!/usr/bin/python
file = open("temp.txt", "r")
read = file.read()
file.close()
file = open("tempout.txt", "w")
for letter in read:
    if letter != " " and letter != "\n" and letter != "\t":
        file.write(letter)
file.close()

