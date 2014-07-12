import timeit
from random import randrange
def small(a):
	amin = a[0]
	for i in a:
		issmallest = True
		for j in a:
			if i>j:
				issmallest = False
		if issmallest:
			amin = i
	return amin	
for i in xrange(1000,10001,1000):
	a = [randrange(100000) for x in range(i)]
	t = timeit.Timer("small(a)","from __main__ import small,a")
	p = t.timeit(number=10)
	print "\nFor no. of element %d the program takes %10.5f seconds"%(i,p)
	print "Min Element=",small(a)


