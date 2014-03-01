#------------------------
#
# Check for a palindrome
#
#-------------------------

input = raw_input("Enter a string to see if its a palindrome: ")

input = input.lower()

reversed_list = []

for letter in reversed(input):
	reversed_list.append(letter)
	
output  = "".join(reversed_list)

if input == output:
	print "It's a palindrome!"
else:
	print "denied - not a palindrome."
	
