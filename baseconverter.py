from adt.Stack import Stack

def baseconverter(n,b):
	m = Stack()
	digits = "0123456789ABCDEF"
	while n > 0:
		m.push(n%b)
		n = n/b
	string = ""
	while not m.isEmpty():
		string = string + digits[m.pop()]
	return string
print baseconverter(233,8)
print baseconverter(233,16)