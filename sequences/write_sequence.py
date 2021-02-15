#!/anaconda3/bin/python3
_sequence = open("sequence.txt", "r")
sequence = _sequence.read()
_sequence.close()
_title = open("title.txt", "r")
title = _title.read()
_title.close()
raw_sequence = open(f"/Users/scottmolloy/Desktop/.alfredWork/FreeVariables/{title}.txt", "w")
raw_sequence.write(sequence)
raw_sequence.close()
def printkey(key):
    out = ""
    out = out+f"keyboard.press(Key.{key})\n"
    out = out+f"keyboard.release(Key.{key})\n"
    out = out+"time.sleep(.1)\ncheck()\n"
    return out
def compound_word(compounds):
    saved_words = ["tab", "shift", "cmd", "alt", "space", "enter", "esc", "down", "up", "left", "right", "delete", "f0", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9"]
    count = len(compounds)
    key1 = compounds[0]
    key2 = compounds[1]
    if count == 2:
        if key2 in saved_words:
            out = f"""with keyboard.pressed(Key.{key1}):
    keyboard.press(Key.{key2})
    keyboard.release(Key.{key2})\n"""
        else:
            out = f"""with keyboard.pressed(Key.{key1}):
    keyboard.press(\"{key2}\")
    keyboard.release(\"{key2}\")\n"""
    else:
        key3 = compounds[2]
        if count == 3:
            if key3 in saved_words:
                out = f"""with keyboard.pressed(Key.{key1}):
    with keyboard.pressed(Key.{key2}):
        keyboard.press(Key.{key3})
        keyboard.release(Key.{key3})\n"""
            else:
                out = f"""with keyboard.pressed(Key.{key1}):
    with keyboard.pressed(Key.{key2}):
        keyboard.press(\"{key3}\")
        keyboard.release(\"{key3}\")\n"""
        else:
            key4 = compounds[3]
            if count == 4:
                if key4 in saved_words:
                    out = f"""with keyboard.pressed(Key.{key1}):
    with keyboard.pressed(Key.{key2}):
        with keyboard.pressed(Key.{key3}):
            keyboard.press(Key.{key4})
            keyboard.release(Key.{key4})"""
                else:
                        out = f"""with keyboard.pressed(Key.{key1}):
    with keyboard.pressed(Key.{key2}):
        with keyboard.pressed(Key.{key3}):
            keyboard.press(\"{key4}\")
            keyboard.release(\"{key4}\")\n"""
            else:
                key5 = compounds[4]
                if count == 5:
                    if key5 in saved_words:
                        out = f"""with keyboard.pressed(Key.{key1}):
    with keyboard.pressed(Key.{key2}):
        with keyboard.pressed(Key.{key3}):
            with keyboard.pressed(Key.{key4}):
                keyboard.press(Key.{key5})
                keyboard.release(Key.{key5})"""
                    else:
                        out = f"""with keyboard.pressed(Key.{key1}):
    with keyboard.pressed(Key.{key2}):
        with keyboard.pressed(Key.{key3}):
            with keyboard.pressed(Key.{key4}):
                keyboard.press(\"{key5}\")
                keyboard.release(\"{key5}\")\n"""
    return out
def translate(word):
    out = ""
    saved_words = ["tab", "shift", "cmd", "alt", "space", "enter", "esc", "down", "up", "left", "right", "delete", "f0", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9"]
    if word == "pause":
        return "time.sleep(.5)\ncheck()\n"
    if word[0:2] == "./":
        if word[2:9] == "pocket/":
            script = "/Users/scottmolloy/.pocketdimension/"+ word[9:]+".py"
        elif len(word) == 4 and word[2] == "s" and word[3] in ["0","1","2","3","4","5","6","7","8","9"]:
            script = "/Users/scottmolloy/Desktop/.alfredWork/sequences/perform_"+word[2:]+"_sequence.py"
        else:
            script = "/Users/scottmolloy/Desktop/.alfredWork/functions/"+word[2:]+".py"
        return f"exec(open('{script}').read())\n"
    if "–" in word:
        compounds = word.split("–")
        out = compound_word(compounds)
        out = out+"time.sleep(.3)\ncheck()\n"
        return out
    if word in saved_words:
        out = out + printkey(word)
    else:
        out = out+f"keyboard.type(\"{word}\")\n"
    return out
sequence = sequence.split(" ")
header = "#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3\n"
header = header+"from pynput.keyboard import Key, Controller\n"
header = header+"keyboard = Controller()\n"
header = header+"import time\n"
header = header+"""def check():
    file = open("ripcord.txt", "r")
    file.close()\n"""
out = ""
for i in range(len(sequence)):
    out = out + translate(sequence[i])
out = header + out
out = out.replace("\n\")", "\")")
out = out.replace("keyboard.press(\"tab\")", "keyboard.press(Key.tab)")
out = out.replace("keyboard.press(\"tab\")", "keyboard.press(Key.tab)")
out = out.replace("keyboard.press(\"shift\")", "keyboard.press(Key.shift)")
out = out.replace("keyboard.press(\"cmd\")", "keyboard.press(Key.cmd)")
out = out.replace("keyboard.press(\"alt\")", "keyboard.press(Key.alt)")
out = out.replace("keyboard.press(\"space\")", "keyboard.press(Key.space)")
out = out.replace("keyboard.press(\"enter\")", "keyboard.press(Key.enter)")
out = out.replace("keyboard.release(\"tab\")", "keyboard.release(Key.tab)")
out = out.replace("keyboard.release(\"tab\")", "keyboard.release(Key.tab)")
out = out.replace("keyboard.release(\"shift\")", "keyboard.release(Key.shift)")
out = out.replace("keyboard.release(\"cmd\")", "keyboard.release(Key.cmd)")
out = out.replace("keyboard.release(\"alt\")", "keyboard.release(Key.alt)")
out = out.replace("keyboard.release(\"space\")", "keyboard.release(Key.space)")
out = out.replace("keyboard.release(\"enter\")", "keyboard.release(Key.enter)")
out = out.replace("""time.sleep(.3)\ncheck()
with keyboard.pressed(Key.ctrl):""", """time.sleep(.8)\ncheck()
with keyboard.pressed(Key.ctrl):""")
_perform_sequence = open(f"perform_{title}_sequence.py", "w")
_perform_sequence.write(out)
_perform_sequence.close()