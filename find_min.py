import timeit
from random import randrange
def small(a):
	min = a[0]
	for i in xrange(len(a)):
		if a[i]<min:
			min = a[i]
	return min
for i in xrange(1000,10001,1000):
	a = [randrange(100000) for x in xrange(i)]
	t = timeit.Timer("small(a)","from __main__ import small,a")
	p = t.timeit(number=10)
	print "\nFor no. of %d elements the program takes %2.5f seconds"%(i,p)
	print "Minimum Element:",small(a)