string1 = list(raw_input())
string2 = list(raw_input())
def check(s1,s2):
	if len(s1) != len(s2):
		return False
	else:
		s3 = []
		for char in s1:
			if char in s2:
				temp = s2.index(char)
				s2.pop(temp)
		if s2 == []:
			return True
print 'yes' if check(string1,string2) else 'No'