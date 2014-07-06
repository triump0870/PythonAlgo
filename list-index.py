import timeit
for i in xrange(100000,10000001,200000):
    list_index = timeit.Timer("x.index(100)","from __main__ import x")
    x = list(xrange(i))
    pi = list_index.timeit(number=1000)
    print "%d, %10.5f"%(i,pi)
