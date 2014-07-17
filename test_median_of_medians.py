import timeit
from random import randrange
def Select(a,j):
	'''Returns the median of the list 'a'.'''
	if len(a)<10:		#if the list size is less then 10 there is no need to call the function again rather sort it using the python builtin function sorted() and return the kth element in the list.
		return sorted(a)[j-1]
	median = []
	k = 0
	s = []
	while k+5<len(a)-1:
		s.append(a[k:k+5])
		k += 5
	s.append(a[k:])
	for sub in s:
		median.append(Select(sub,(len(sub)-1)/2))
	M = Select(median,(len(median)-1)/2)
	l1 = [] 		#For elements less then M
	l2 = []			#For elements greater than M
	for i in a:
		if i<M:
			l1.append(i)
		else:
			l2.append(i)	

	if j < len(l1):
		return Select(l1,j)	
	elif j> (len(l1)+1):
		return Select(l2,j-len(l1)-1)
	else:
		return M
def kth(k):
	'''Return the appropriate suffix for kth position element.'''
	if k==1:return '1st' 
	elif k==2:return '2nd' 
	elif k==3:return '3rd'  
	else:return str(k)+'th'

for i in xrange(1000,10001,1000):
	a = list(xrange(randrange(i)))
	x = randrange(100)
	t = timeit.Timer("Select(a,x)","from __main__ import a,Select,x")
	p = t.timeit(number=1000)
	print "%d, %10.5f seconds %s"%(i,p,Select(a,x))