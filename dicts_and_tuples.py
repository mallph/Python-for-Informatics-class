# PJ Mallery
# Assignment 5
# python 3

import sys
fname = input('Enter mbox or mbox-variant filename: ') 

try:
    fhand = open(fname)
except:
    print('Could not find specified file. Please ensure filename is correct and/or the file is in the directory.')
    sys.exit(0)
    
d = dict()  # initalize empty dictionary for email addresses before iterating
for line in fhand:
    if not line.startswith('From '): continue  # included space to ignore possible 'From:' lines in file
    words = line.split()
    d[words[1]] = d.get(words[1], 0) + 1

tlist = list()
for key, val in d.items():
    tlist.append((val, key))  # extra set of parentheses to create tuple; value before key for sorting purposes 

tlist.sort(reverse=True)
most = tlist[0]
print('The address with the most messages is', most[1], 'with', most[0], 'messages.')
