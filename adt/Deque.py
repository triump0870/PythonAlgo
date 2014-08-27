'''Author: Rohan Roy
Description: A deque, also known as a double-ended queue, is an ordered collection of items similar to the queue.
It has two ends, a front and a rear, and the items remain positioned in the collection.
What makes a deque different is the unrestrictive nature of adding and removing items.
New items can be added at either the front or the rear. Likewise, existing items can be removed from either end.
In a sense, this hybrid linear structure provides all the capabilities of stacks and queues in a single data structure. 
'''
class Deque:
	def __init__(self):
		"Creates a new deque that is empty. It needs no parameters and returns an empty deque."
		self.items = []

	def addFront(self, item):
		"Adds a new item to the front of the deque. It needs the item and returns nothing."
		return self.items.append(item)

	def addRear(self, item):
		"Adds a new item to the rear of the deque. It needs the item and returns nothing."
		return self.items.insert(0,item)

	def removeFront(self):
		"Removes the front item from the deque. It needs no parameters and returns the item. The deque is modified."
		return self.items.pop()

	def removeRear(self):
		"Removes the rear item from the deque. It needs no parameters and returns the item. The deque is modified."
		return self.items.pop(0)

	def isEmpty(self):
		"Tests to see whether the deque is empty. It needs no parameters and returns a boolean value."
		return self.items == []

	def size(self):
		"Returns the number of items in the deque. It needs no parameters and returns an integer."
		return len(self.items)

	def values(self):
		"Returns the items in the Deque."
		return self.items
