from adt.Stack import Stack
from sys import stdin
def paren(string):
	top = Stack()
	matched = True
	index = 0
	while index <len(string) and matched>0:
		symbol = string[index]
		if symbol == "(":
			top.push(symbol)
		else:
			if top.isEmpty():
				matched = False
			else:
				top.pop()
		index += 1
	if matched and top.isEmpty():
		return True
	else:
		return False
string = '()()'
print paren(string)