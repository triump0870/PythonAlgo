from adt.Stack import Stack
m = Stack()
s = raw_input()
for char in s:
	m.push(char)
l = m.size()
t = [m.pop() for x in xrange(l)]
print ''.join(t)

