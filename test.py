import time

def sumofn(n):
	start= time.time()
	s = n*(n+1)/2
	end = time.time()
	return s,end-start