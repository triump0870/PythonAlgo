#!/usr/bin/env python
from adt.Stack import Stack

def infix_to_postfix(infix):
	"Converts the infix notation into postfix notation."
	opstack = Stack()
	output = []
	op= "abcdefghijklmnopqrstuvwxyz"
	oprand = op + op.upper() + "0123456789"
	operator = "+-*/"
	paren = "()"
	infix = infix.split()
	pre = {}
	pre['*'] = 3
	pre['/'] = 3
	pre['+'] = 2
	pre['-'] = 2
	pre['('] = 1

	for j in infix:
		if j in oprand:
			print j
			output.append(j)
		elif j == '(':
			opstack.push(j)
		elif j == ')':
			top = opstack.pop() 
			while top != '(':
				output.append(top)
				top = opstack.pop()
		else:
			while not opstack.isEmpty() and pre[opstack.peek()] >= pre[j]:
				top = opstack.pop()
				output.append(top)
				print top
			opstack.push(j)
	while not opstack.isEmpty():
		output.append(opstack.pop())
	return ' '.join(output)

