# PJ Mallery
# Assignment 5
# python 3

fname = 'mbox.txt'
# come back to update with user input with try/except
fhand = open(fname)
d = dict()
for line in fhand:
	if not line.startswith('From '):continue
	words = line.split()
	d[words[1]] = d.get(words[1],0) + 1

tlist = list()
for key, val in d.items():
	tlist.append((val, key))

tlist.sort(reverse=True)
most = tlist[0]
print('The address with the most messages is', most[1], 'with', most[0], 'messages.')
