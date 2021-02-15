#!/anaconda3/bin/python3

import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/Users/scottmolloy/.pocketdimension')

import hello
import assorted
from assorted import file as get
from assorted import touch as touch
from assorted import assignment_file as assign
from assorted import assignment_vfile as assignv
from assorted import assignment_vfilec as assignvc
from assorted import fetch_free_variable as fetch

sequence = get("sequence")
sequence = sequence.split(" ")
for i in range(len(sequence)):
    if sequence[i] == "•tap":
        sequence[i] = f"cmd–f {sequence[i+1]}"
        sequence[i+1] = "esc enter"
space = " "
sequence = space.join(sequence)
sequence = sequence.replace("•left", "cmd–alt–left")
sequence = sequence.replace("•right", "cmd–alt–right")
sequence = sequence.replace("ªleft", "alt–left")
sequence = sequence.replace("ªright", "alt–right")
sequence = sequence.replace("·left", "shift–alt–left")
sequence = sequence.replace("·right", "shift–alt–right")
sequence = sequence.replace("ºleft", "cmd–left")
sequence = sequence.replace("ºright", "cmd–right")
sequence = sequence.replace("‚left", "shift–cmd–left")
sequence = sequence.replace("‚right", "shift–cmd–right")
sequence = sequence.replace("•findNext", "cmd–f ctrl–v pause esc")
sequence = sequence.replace("•click", "ctrl–y")
sequence = sequence.replace("•paste", "ctrl–v")
sequence = sequence.replace("•copy", "alt–ctrl–c")

thing = f"sequence = {sequence}"
assign(thing)