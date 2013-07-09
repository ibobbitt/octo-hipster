#!/usr/bin/python

import sys
import itertools

def get_pairs(l):
    if len(l) < 2:
        yield l
        return
    a = l[0]
    for i in range(1,len(l)):
        pair = (a,l[i])
        for rest in get_pairs(l[1:i]+l[i+1:]):
            yield [pair] + rest

def f(a,b,l):
	for c,d in l:
		if a == c and b == d:
			return False
	return True

people = [line.strip() for line in open(sys.argv[1])]
events = [line.strip() for line in open(sys.argv[2])]
pairings = list(get_pairs(people))

if len(events) >= len(people):
	print "Too many events (%d) for number of people (%d). Reduce to at most %d event(s)." % (len(events), len(people), len(people) - 1)
	exit(0)

for ev in events:
	order = pairings.pop()
	print ev
	for a,b in order:
		pairings = filter((lambda x: f(a,b,x)), pairings)
		print "\t%s, %s" %(a,b)
	print
