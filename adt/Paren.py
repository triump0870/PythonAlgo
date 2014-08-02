from Stack import Stack
def check(string):
	m = Stack()
	balanced = True
	index = 0
	while index < len(string) and balanced:
		symbol = string[index]
		if symbol in "({[":
			m.push(symbol)
		else:
			if m.isEmpty():
				balanced =False
			else:
				top = m.pop()
				if not matched(top,symbol):
					balanced = False
		index += 1
	if balanced and m.isEmpty():
		return 'True'
	else:
		return 'False'

def matched(open,close):
	opens = "({["
	closers = ")}]"
	return opens.index(open) == closers.index(close)