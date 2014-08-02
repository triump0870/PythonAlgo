from timeit import Timer
import timeit
from random import randrange

def gcd(a,b):
	while b:
		a,b = b,a%b
	return a

def test():
	"This is the test module."
	assert gcd(40,17) == 1
	assert gcd(21,3) == 3
	assert gcd(2,0) == 2
	assert gcd(0,3) == 3

	return "Tests passes"
t = Timer("gcd(a,b)","from __main__ import a,b,gcd")
sum = 0
for i in xrange(1000000,100000001,1000000):
	a = randrange(100000,1000001)
	b = randrange(100000,1000001)
	p = t.timeit(number = 100000)
	sum += p
	print "%d %5.5f miliseconds"%(i,p*1000)
print "total time:",sum