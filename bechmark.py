import time

def Bench(n):
	start = time.time()
	sum = 0
	for i in xrange(1,n+1):
		sum += i

	end = time.time()
	return sum,(end-start)*1000

for i in xrange(5):
	print "Sum is %d required %10.7f miliseconds"%Bench(1000000)