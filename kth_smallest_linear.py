import timeit
from random import randrange
def smallest(k,a):
	amin = min(a)
	for i in a:
		if i <min and k!==0:
			min = i
			k -= 1
		