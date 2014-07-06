import timeit
from timeit import Timer
pop_end = Timer("x.pop()","from __main__ import x")
pop_zero = Timer("x.pop(0)","from __main__ import x")

print "pop(0) pop()"
for i in xrange(1000000,100000001,1000000):
    x = list(xrange(i))
    pz =  pop_zero.timeit(number=1000)
    x = list(xrange(i))
    pt = pop_end.timeit(number=1000)
    print "%15.5f, %15.5f"%(pz,pt)
