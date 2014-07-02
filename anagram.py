string1 = raw_input()
string2 = raw_input()
def check(s1,s2):
	if len(s1) != len(s2):
		return False
	else:
		s3 = []
		for char in s1:
			if char in s2:
				s3.append(char)
		a = s1.strip('\r')
		b = ''.join(s3)
		if a == b:
			return True
print 'yes' if check(string1,string2) else 'No'