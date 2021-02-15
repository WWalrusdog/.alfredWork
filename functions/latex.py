#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip as p
prev_clip = open("/Users/scottmolloy/Desktop/.alfredWork/functions/previous_clip.txt", "r")
content = prev_clip.read()

def latex(example):
    example = example.split(" ")
    i = 0
    rbrack = "}"
    lbrack = "{"
    while(i<len(example)):
        if "/" in example[i]:
            example[i] = example[i].split("/")
            example[i] = f"\\frac{lbrack}{example[i][0]}{rbrack}{lbrack}{example[i][1]}{rbrack}"
        if "_" in example[i]:
            example[i] = example[i].split("_")
            example[i] = f"{example[i][0]}_{lbrack}{example[i][1]}{rbrack}"
        if "^" in example[i]:
            example[i] = example[i].split("^")
            example[i] = f"{example[i][0]}^{lbrack}{example[i][1]}{rbrack}"
        i += 1
    example = " ".join(example)
    return(example.replace("(","\\left(").replace(")","\\right)"))

p.copy(latex(content))	