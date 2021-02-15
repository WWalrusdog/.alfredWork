#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from pathlib import Path
import pyperclip as p

def capsEncode(word):
    codedWord = ""
    for i in range(len(word)):
        if (word[i] >= 'A' and word[i] <= 'Z'): 
            codedWord = codedWord+"↑"+word[i]
        else:
            codedWord = codedWord+word[i]
    return(codedWord)

def retrieveData(title):
    if Path(f"/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/{title}.txt").is_file():
        return(open(f"/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/{title}.txt").read())
    elif Path(f"/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/url/{title}.txt").is_file():
        return(open(f"/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/url/{title}.txt").read())
    elif Path(f"/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/latin/{title}.txt").is_file():
        return(open(f"/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/latin/{title}.txt").read())
    elif Path(f"/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/unicodeExpanded/{title}.txt").is_file():
        return(open(f"/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/unicodeExpanded/{title}.txt").read())
    elif Path(f"/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/programmingShorts/{title}.txt").is_file():
        return(open(f"/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/programmingShorts/{title}.txt").read())
    elif Path(f"/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/constants/{title}.txt").is_file():
        return(open(f"/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/constants/{title}.txt").read())
    elif Path(f"/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/states/{title}.txt").is_file():
        return(open(f"/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/states/{title}.txt").read())
    
def fetch_var():
    term = p.paste().strip(" ")
    content = retrieveData(capsEncode(term))
    lowerContent = retrieveData(term)
    if content:
        return content+" "
    elif lowerContent:
        return lowerContent+" "
    else:
        return term
p.copy(fetch_var())