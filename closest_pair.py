import math, pprint

pts = [(1,2), (12,8), (22,1), (36,22), (18, 11)]

"""subtract x from x, y from y and then square root of x square + y square for distance, then get min"""

def dist( a, b ):
	xdist = b[0]-a[0]
	ydist = b[1]-a[1]
	
	return math.sqrt(xdist**2 + ydist**2)

# roll through the list of points

min = dist(pts[0], pts[1])
minPts = ( pts[0], pts[1] )

for i in range( len(pts) ):
	for j in range( i+1, len(pts) ):
		test = dist( pts[i], pts[j] )
#		print test
		if test < min:
			minPts = ( pts[i], pts[j] )
			min = test

pprint.pprint( minPts ) 
print "distance is %f" % min
		