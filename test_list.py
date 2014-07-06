from timeit import Timer
import timeit
def test1():
    l = []
    for i in xrange(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in xrange(1000)]

def test4():
    l = list(xrange(1000))

t1 = Timer("test1()","from __main__ import test1")
print "Concat ",t1.timeit(number=1000),"miliseconds"
t2 = Timer("test2()","from __main__ import test2")
print "Append ", t1.timeit(number=1000),"miliseconds"
m = "miliseconds"
n = 1000
t3 = Timer("test3()","from __main__ import test3")
print "Comprehension ",t3.timeit(n), m
t4 = Timer("test4()","from __main__ import test4")
print "List range ",t4.timeit(n),m
