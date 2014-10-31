#!/usr/bin/env python
'''Author: Rohan Roy
Description: This is a program to implement Queue in Python.
'''

class Queue:
	"This is the Queue implementation class."
	def __init__(self):
		"Initialize an empty Queue."
		self.items = []

	def enqueue(self,item):
		"Adds a new item to the rear of the Queue."
		self.items.insert(0,item)

	def dequeue(self):
		"Removes the front item from the queue."
		return self.items.pop()

	def isEmpty(self):
		"Tests to see whether the queue is empty."
		return self.items == []

	def size(self):
		"Returns the size of the queue."
		return len(self.items)
