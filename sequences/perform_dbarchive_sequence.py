#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from pynput.keyboard import Key, Controller
keyboard = Controller()
import time
keyboard.type("ssh")
keyboard.type("{r1}.prod\ncd")
keyboard.type("/usr/docroot/site_archive\ncp")
keyboard.type("archive.tgz")
keyboard.type("~/archive.tgz\nsftp")
keyboard.type("{r1}.prod\ntar")
keyboard.type("xvzf")
keyboard.type("archive.tgz\ncd")
keyboard.type("drupal/\ncd")
keyboard.type("newspace/")
