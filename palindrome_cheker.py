from adt.Deque import Deque

def cheker(string):
	d = Deque()
	for i in string:
		d.addFront(i)
	stillequal = True
	while d.size() > 1 and stillequal:
		if d.removeRear() != d.removeFront():
			stillequal = False
	return stillequal

string = raw_input()
print cheker(string)