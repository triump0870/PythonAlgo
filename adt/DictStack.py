'''Author: Rohan roy
Description: This is the implementation of Stack using dictionary.
'''
class Stack:
	def __init__(self):
		self.items = {}

	def push(self, item):
		self.items[len(self.items)] = item

	def pop(self):
		item = self.items[len(self.items)-1]
		del self.items[len(self.items)-1]
		return item

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

	def isEmpty(self):
		return self.items == {}
