from adt.Queue import Queue

def hot_potato(namelist, num):
	game = Queue()
	for name in namelist:
		game.enqueue(name)

	while game.size() > 1:
		for i in xrange(num):
			
			game.enqueue(game.dequeue())
			
		player=game.dequeue()
		print player
	return game.dequeue()

print('Winner is:',hot_potato(["Bill","David","Susan","Jane","Kent","Brad"],7))
