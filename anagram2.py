import time
def anagram(a,b):
	start = time.time()
	a.sort()
	b.sort()
	s = False
	if ''.join(a) == ''.join(b):
		s =  True
	end = time.time()
	print "%15.10f"%(end-start)
	return s

s1 = list(raw_input())
s2 = list(raw_input())
print 'Yes' if anagram(s1,s2) else 'No'