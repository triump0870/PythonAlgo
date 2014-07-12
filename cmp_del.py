import timeit
from random import randrange
def list_del(x):
    del x[randrange(90000)]
def dict_del(x):
	try:
		del x[randrange(90000)]
	except KeyError:
		pass

for i in xrange(100000,10000001,200000):
    x = list(xrange(i))
    t = timeit.Timer("list_del(x)","from __main__ import list_del,x")
    r = {j:None for j in xrange(i)}
    d = timeit.Timer("dict_del(r)","from __main__ import dict_del,r")
    pt = t.timeit(number =1000)
    pd = d.timeit(number = 1000)
    print "%d,%10.5f,%10.5f"%(i,pt,pd)
