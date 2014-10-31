from random import randrange
from adt.Queue import Queue

class Printer:
	def __init__(self,ppm):
		self.pagerate = ppm
		self.currentTask = None
		self.timeRemaining = 0

	def tick(self):
		if self.currentTask != None:
			self.timeRemaining = self.timeRemaining -1
			if self.timeRemaining <= 0:
				self.currentTask = None

	def busy(self):
		if self.currentTask != None:
			return True
		else:
			return False

	def startNext(self,newtask):
		self.currentTask = newtask
		self.timeRemaining = newtask.getPages() * 60/self.pagerate

class Task:

	def __init__(self,time):
		self.timestamp = time
		self.pages = randrange(1,21)

	def getStamp(self):
		return self.timestamp

	def getPages(self):
		return self.pages

	def waitTime(self, currenttime):
		return currenttime - self.timestamp

def simulation(numSeconds, pagesPerMinute, numStudent):
	labprinter = Printer(pagesPerMinute)
	printQueue = Queue()
	waitingtimes = []

	for currentSecond in xrange(numSeconds):
		if newPrintTask(numStudent):
			task = Task(currentSecond)
			printQueue.enqueue(task)

		if (not labprinter.busy()) and (not printQueue.isEmpty()):
			nexttask = printQueue.dequeue()
			waitingtimes.append(nexttask.waitTime(currentSecond))
			labprinter.startNext(nexttask)

		labprinter.tick()

	avarageWait = sum(waitingtimes)/len(waitingtimes)
	print "Average Wait %6.2f secs %3d tasks remaining."%(avarageWait, printQueue.size())

def newPrintTask(student):
	maxt = 3600/(student*2)
	num = randrange(1, maxt+1)
	if num == maxt:
		return True
	else:
		return False

for i in xrange(10):
	simulation(3600,10,20)