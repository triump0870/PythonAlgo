import timeit as t
from random import randrange as r
def l(a,m):
	x = list(a[i] for i in xrange(len(a)) if a[i] < m)
	return x
def c(a,m):
	x = [a[i] for i in xrange(len(a)) if a[i] < m]
	return x

for i in xrange(1000,10001,1000):
	a = list(xrange(i))
	m = r(i)
	ls = t.Timer("l(a,m)","from __main__ import a,m,l")
	cs = t.Timer("c(a,m)","from __main__ import a,m,c")
	lt = ls.timeit(number=1000)
	ct = cs.timeit(number=1000)
	print "%d list takes=%4.5f and comprehension takes=%4.5f"%(i,lt,ct)