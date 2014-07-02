import time 
start = time.time()
a = [3,4,55,6,7,87,2,90,12,11,23,34,3453,2342,24,213,123,23,214,214,214,21421,421,4214,214,214,214,21,421,421,1,124,21,543,6,3,6,356,34,634,643,64,43545,346,124,3,414]
min = a[0]
for i in xrange(len(a)):
	if a[i]<min:
		min = a[i]

print min
end = time.time()
elp = (end-start)*1000
print 'time=%10.7f'%elp,"miliseconds"