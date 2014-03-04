#------------------------------------------------------------------------
# sorting
#	pythons - list.sort (binary for small arrays and merge for larger)
# 	bubble
#	pure python merge 
#------------------------------------------------------------------------
import random
import time

#-------------------------
# create our random list
#-------------------------
l = []

for i in range( 0, 1000 ):
	l.append(random.randint(1,1000))

print l

#--------------------
# py sort
#--------------------
t1 = list(l)
start = time.clock()
t1.sort()
py_sort_time = ( time.clock() - start )


#---------------------
# bubble sort
#---------------------
t2 = list(l)

start = time.clock()
changed = True

while changed:
	changed = False
	for x in range( 0, len(t2)-1 ):
		if t2[x] > t2[x+1]:
			changed = True
			temp = t2[x+1]
			t2[x+1] = t2[x]
			t2[x] = temp
			
bubble_sort_time = (time.clock() - start )

print "python: ", py_sort_time
print "bubble: ", bubble_sort_time


	