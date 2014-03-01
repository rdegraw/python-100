#-----------------------------------------------------
#
# Find the next prime number as the user keeps asking
#
#-----------------------------------------------------
import sys

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
if __name__ == "__main__":
	
	curr_prime = 1	#initialize the prime number
	
	while True:
		response = raw_input( "Print the next prime? [Y]es " )
		if response.upper().startswith('Y'):
			while True:
				curr_prime += 1
				if is_prime(curr_prime):
					print curr_prime
					break
		else:
			break
		


