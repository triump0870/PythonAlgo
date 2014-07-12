import timeit
x = {}
def set_item():
    for i in xrange(100000):
        x.__setitem__(i,50)

def get_item():
    for i in xrange(100000):
        x.__getitem__(i)
t1 = timeit.Timer("set_item()","from __main__ import set_item")
t2 = timeit.Timer("get_item()","from __main__ import get_item")
for i in xrange(100000):
    s = t1.timeit(number=1000)
    g = t2.timeit(number=1000)
    print "%10.5f, %10.5f"%(s,g)
