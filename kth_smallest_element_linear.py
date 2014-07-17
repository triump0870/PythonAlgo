def Select(a,n):
	'''Returns the nth smallest element for an unsorted list of unique elements.'''
	if len(a)<10:		#if the list size is less then 10 there is no need to call the function again rather sort it using the python builtin function sorted() and return the kth element in the list.
		return sorted(a)[n-1]
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

	if n < len(l1):
		return Select(l1,n)	
	elif n> (len(l1)+1):
		return Select(l2,n-len(l1)-1)
	else:
		return M
def kth(k):
	'''Return the appropriate suffix for kth position element.'''
	if k==1:return '1st' 
	elif k==2:return '2nd' 
	elif k==3:return '3rd'  
	else:return str(k)+'th'

print "\n\n=================================================================="
print "==========================Median Of Medians======================="
print "=================================================================="
print '''Author: Rohan Roy
Title: Median Of Medians Algorithm
Time Complexity: O(n) (Worst-Case)
Description: This code demonstrates the Median Of Medians Algorithm
in Python. It takes list entries and the kth position entry and then
makes the list entries unique by calling the Python builtin function
set().It computes the medians recursively and returns the kth element.'''
print "=================================================================="
a = list(map(int,raw_input("Enter the array entries:").split()))
print "=================================================================="
print "The sorted List:",list(set(sorted(a)))
print "=================================================================="
k = input("Enter the value of k:")
print "=================================================================="
print "The {0} smallest element is:{1}".format(kth(k),Select(list(set(a)),k))
print "=================================================================="
