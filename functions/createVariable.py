#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from pathlib import Path
import pyperclip as p

states = ["count", "delimeter", "form"]
latin = ["alpha","beta","gamma","delta","epsilon","zeta","eta","theta","iota","kappa","lambda","omikron","rho","sigma","tau","upsilon","phi","chi","psi","omega","mu","nu", "theta"]




def checkCollections(title):
    refTitle = title.replace("↑","")
    if refTitle[0:3].lower() == "url":
        title = "url/" + title
    elif refTitle in states:
        title = f"states/{title}"
    elif refTitle[0:5].lower() == "latin":
        title = f"latin/{title[5:]}" 
    elif refTitle in latin:
        title = f"latin/{title}" 
    elif refTitle in states:
        title = f"programmingShorts/{title}"
    elif refTitle[0:7].lower() == "unicode":
        title = f"unicodeExpanded/{title[7:]}"
    return title
        

def capsEncode(word):
    codedWord = ""
    for i in range(len(word)):
        if (word[i] >= 'A' and word[i] <= 'Z'): 
            codedWord = codedWord+"↑"+word[i]
        else:
            codedWord = codedWord+word[i]
    return(codedWord)

def assign(example):
    example = example.split("=")
    title = capsEncode(checkCollections(example[0].strip(" ")))
    content = "=".join(example[1:]).strip(" ")
    open(f"/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/{title}.txt", "w").write(content)
    open(f"/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/lastCreated.txt", "w").write(content)
    open(f"/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/lastCreatedTitle.txt", "w").write(title)

assign(p.paste())