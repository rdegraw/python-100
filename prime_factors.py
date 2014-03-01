#--------------------------------------------------
#
# Find all the prime factors up to a given number
#
#--------------------------------------------------

#------------------------
# is the number a prime?
#------------------------
def is_prime( num ):
	for i in range( 2, num ):
		if num % i == 0:
			return False
	if num != 1:
		return True
	else:
		return False

	
#--------------------
# main
#--------------------
value = int( raw_input( "What number do you want me to check? " ))

for i in range( 2, value+1 ):
	if is_prime(i):
		
		#-------------
		# is factor?
		#-------------
		if( value % i == 0 ):
			print i


