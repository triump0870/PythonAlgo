'''Author: Rohan Roy
Title: Stack
Description: This is a python implementation of ADT Stack
Disclaimer: Do not copy it. Respect coders to gian respect.
'''
class Stack:
	'''This is the Stack datastructure with the basic operetions.'''

	def __init__(self):
		#Initializes a empty stack
		self.items = []

	def isEmpty(self):
		#Return True if the stack is empty
		return self.items == []

	def push(self,item):
		#Inserts the item into the stack
		self.items.append(item)

	def pop(self):
		#Retruns the top item i.e the last item from the stack after removing it
		return self.items.pop()

	def peek(self):
		#Retruns the top i.e the last item from the stack with out removing the item from the stack
		return self.items[-1]

	def size(self):
		#Returns the size of the stack
		return len(self.items)
