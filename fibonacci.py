#----------------------------------------
#
# Fibonacci number to the nth position
#
#----------------------------------------


position = int( raw_input( "Please enter the number of Fibonacci values you would like to print: " ))

sequence = [0]

while len(sequence) < position:
	# F(n) = F(n-1) + F(n-2)
	if len(sequence) == 1:
		sequence.append(1)
	else:
		sequence.append( sequence[-2] + sequence[-1])
	
print sequence
