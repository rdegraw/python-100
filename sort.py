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

for i in range( 0, 5000 ):
	l.append(random.randint(1,5000))

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
			t2[x], t2[x+1] = t2[x+1], t2[x]
		#	temp = t2[x+1]
		#	t2[x+1] = t2[x]
		#	t2[x] = temp
			
bubble_sort_time = (time.clock() - start )


#------------------------
# merge sort - found improvs on stack overflow   
#------------------------
t3 = list(l)

start = time.clock()

def msort(x):
	result = []
	if len(x) < 2:
		return x
	mid = int(len(x)/2)
	y = msort(x[:mid])
	z = msort(x[mid:])
	i = 0
	j = 0
	while i < len(y) and j < len(z):
		if y[i] > z[j]:
			result.append(z[j])
			j += 1
		else:
			result.append(y[i])
			i += 1
	result += y[i:]
	result += z[j:]
	return result

msort( t3 )

merge_sort_time = (time.clock() - start )

print "python: ", py_sort_time
print "bubble: ", bubble_sort_time
print "merge: ", merge_sort_time

	