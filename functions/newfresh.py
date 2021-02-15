#!/anaconda3/bin/python3
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
keyboard.type("hjkl f")