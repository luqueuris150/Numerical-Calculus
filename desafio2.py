import matplotlib.pyplot as plt
import random

rnd = lambda : random.gauss(0,1)

# input list
# randomized Y vector
X = list(range(10))
Y = [rnd() for k in X]
# data from trigonometric function
#X = [0., 15,    30,    45,    60, 75,    90]
#Y = [1., .9659, .8660, .7071, .5, .2588, .0]
# an arbitraty "symbolic" function
X = list(range(10))
Y = [8*x**2+-x**3+25*x for x in X]
n = len(X)

n_inter = 3


def Lk(x, i):
	lk=1.
	for j in range(n):
		if j == i:
			continue
		lk *= (x-X[j])/(X[i]-X[j])
	return lk

def Pn(x):
	pn=0.
	for i in range(n):
		pn += Y[i]*Lk(x, i)
	return pn


lastXpoint = X[0]
for point in range(1,n):

	dX = X[point]-lastXpoint
	
	interX = [lastXpoint+dX/(n_inter+1)*a for a in range(1,n_inter+1)]
	
	interY = [Pn(x) for x in interX]
	
	plt.scatter(interX, interY, s=10., c='k')

	lastXpoint = X[point]
	
for point in X:
	plt.scatter(point, Pn(point), s=10., c='r')

plt.show()
