#!/usr/bin/env python
'''Author: Rohan Roy
Description: This program evaluates a postfix expression.
'''

from Stack import Stack

def evaluate(infix):
	"Perform the postfix evaluation."
	operandStack = Stack()
	infix = infix.split()
	operand = "0123456789"
	for token in infix:
		if token in operand:
			operandStack.push(int(token))
		else:
			secondOp = operandStack.pop()
			firstOp = operandStack.pop()
			result = doMath(token,firstOp,secondOp)
			operandStack.push(result)
	return operandStack.pop()

def doMath(op,op1,op2):
	"Return the result of the operation between operand1 and operand2."
	if op == '^':
		return op1 ** op2
	elif op == '*':
		return op1 * op2
	elif op == '/':
		return op1/op2
	elif op == '+':
		return op1 + op2
	else:
		return op1 - op2
