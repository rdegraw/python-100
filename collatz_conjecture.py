#--------------------------------------------------
#
# Collatz Conjecture 
#
#--------------------------------------------------
import sys

start = raw_input( "Enter a number to test the Collatz Conjecture: ")

try:
	num = int(start)
except ValueError:
	sys.exit("Should have entered a integer I can deal with")

count = 0

if num > 1:
	while num != 1:
		if (num % 2) == 0:
			num /= 2
		else:
			num = num * 3 + 1
		
		print num
		count += 1
	
	print "It took %d steps" %count
	
else:
	print "number must start greater than 1"

