from adt.Stack import Stack
def convert(n):
	m = Stack()
	while n >0:
		m.push(n%2)
		n = n/2
	string = ""
	while not m.isEmpty():
		string = string + str(m.pop())
	return string

print convert(42)