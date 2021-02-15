#!/anaconda3/bin/python3
_function = open("function.txt", "r")
function = _function.read()
_function.close()
_title = open("title.txt", "r")
title = _title.read()
_title.close()
raw_function = open(f"{title}_raw_function.txt", "w")
raw_function.write(function)
raw_function.close()

out = """#!/anaconda3/bin/python3
from pynput.keyboard import Key, Controller
keyboard = Controller()
import time
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/Users/scottmolloy/.pocketdimension')

from assorted import file as get
from assorted import touch as touch
from assorted import assignment_file as assign
from assorted import assignment_vfile as assignv
from assorted import assignment_vfilec as assignvc
from assorted import fetch_free_variable as fetch
"""
out = out + function

_perform_function = open(f"{title}.py", "w")
_perform_function.write(out)
_perform_function.close()