def AvarageReading(minl,maxl,reading):
	inr = 0
	out = 0
	sum = 0
	count = 0
	for i in reading:
		sum += i
		if minl<=i<=maxl:
			count += 1
			inr += i
		else:
			out += i
			
	s = float("{0:.1f}".format(out/float(sum)))
	if s <=.1:
		return inr/float(count)
	else:
		return float(0.0)
minl = input()
maxl = input()
read = tuple(map(int,raw_input().split()))
print AvarageReading(minl,maxl,read)