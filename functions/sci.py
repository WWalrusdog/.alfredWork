#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip as p
prev_clip = open("/Users/scottmolloy/Desktop/.alfredWork/functions/previous_clip.txt", "r")
content = prev_clip.read()
prev_clip.close()


def sci(num):
    num = float(num)
    sign = ""
    if num < 0:
        num = float(str(num)[1:])
        sign = "-"
    if num > 1 or num < -1:
        num = str(num)
        lead = num[0]
        follow = num[1:]
        i = str(follow).split(".")
        power = len(i[0])
        follow = "".join(i)
        sci = f"{sign}{lead}.{follow}e+{power}"
        return sci
    else:
        i = str(num).split(".")
        i = i[1]
        print(i)
        power = 1
        follow = i
        for j in range(len(i)):
            if i[j] == "0":
                power = power+1
                follow = follow[1:]
            else:
                break;
        sci = f"{sign}{follow[0]}.{follow[1:]}e-{power}"
        return sci

content = sci(content)


p.copy(content)