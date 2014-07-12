import timeit
import random
for i in xrange(10000,1000001,20000):
    t = timeit.Timer("random.randrange(%d) in x"%i,"from __main__ import random,x")
    x = list(xrange(i))
    st = t.timeit(number = 1000)
    x = {j:None for j in xrange(i)}
    d_time = t.timeit(number =1000)
    print "%d,%10.3f,%10.3f"%(i,st,d_time)
