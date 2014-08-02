N = []
V = []
def pack(n):
	if len(n)>=3:
		normal(n)
	else:
		varity(n)
def normal(n):
	global N
	n.pop()
	n.pop()
	n.pop()
	N.append(1)
def varity(n):
	global N,V
	n.pop()
	V.append(1)
	if len(V)==3:
		V.pop()
		V.pop()
		V.pop()
		N.append(1)
def countnormal():
	global N,V
	if r > 0:
		n = len(N)+1
	else:
		n = len(N)
	del N[:]
	del V[:]
	return n

r = input()
g = input()
b = input()
R = ['R' for x in xrange(r)]
G = ['G' for x in xrange(g)]
B = ['B' for x in xrange(b)]
while len(R) >0:
	pack(R)
while len(G)>0:
	pack(G)
while len(B)>0:
	pack(B)
countnormal()