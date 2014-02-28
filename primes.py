#----------------------------------------------
#
# All the prime numbers up to a given number
#
#----------------------------------------------

def isPrime( fac ):
	for i in range( 2, fac ):
		if fac % i == 0:
			return False
	return True

value = int( raw_input( "What number do you want me to go to? " ))

for i in range( 1, value+1 ):
	if isPrime(i):
		print i
