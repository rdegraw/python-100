#--------------------------------------------------
#
# Binary to Decimal and Back Converter 
#
#--------------------------------------------------
import sys
import math

def binary_2_decimal( bin ):
	pos = 0
	dec = 0
	
	for digit in reversed(bin):
		try:
			bit = int (digit)
		except ValueError:
			sys.exit("Binary to decimal conversion broke based on value sent to it!")
		
		if bit == 1:
			dec += 2**pos
		
		pos += 1
		
	return dec

def decimal_2_binary( dec ):
	bin = []
	
	try:
		dec = int (dec)
	except ValueError:
		sys.exit( "Decimal to binary conversion broke based on value sent to it!" )
	
	while dec != 0 :
		bit = str(dec % 2)
		dec /= 2
		bin.append(bit)
	
	bin.reverse()
	final_num = ''.join(bin)
	
	return final_num

	
if __name__ == '__main__':

	# print options to user
	print "convert binary to decimal: 1"
	print "convert decimal to binary: 2"
	
	# check the option type
	choice = None
	while not choice:
		val = raw_input("choice? ")
		try:
			choice = int(val)
		except ValueError:
			print "Must choose an integer 1 or 2 - you typed: ", val
	
	if choice == 1:
		bin = raw_input("Give me a binary number: ")
		dec = binary_2_decimal( bin )
		print "Binary number: ", bin, " converted to decimal: ", dec 
	
	elif choice == 2:
		dec = raw_input("Give me a decimal number: ")
		bin = decimal_2_binary( dec )
		print "Decimal number: ", dec, " converted to binary: ", bin
		
	else:
		print "invalid choice - rtfd (sic)"






