#!/anaconda3/bin/python3

import sys
#insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/Users/scottmolloy/.pocketdimension')


import assorted
from assorted import file as get
from assorted import touch as touch
from assorted import assignment_file as assign
from assorted import assignment_vfile as assignv
from assorted import assignment_vfilec as assignvc
from assorted import fetch_free_variable as fetch

function = get("function")
function = function.replace("print(", "keyboard.type(")


thing = f"function = {function}"
assign(thing)