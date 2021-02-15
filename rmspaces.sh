#!/bin/bash
pbpaste > temp.txt
./rmspaces.py
cat tempout.txt | pbcopy
rm temp.txt tempout.txt
exit
