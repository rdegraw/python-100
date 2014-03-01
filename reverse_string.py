#-------------------
# reverse a string
#-------------------

input = raw_input("Enter a string to reverse: ")

reversed_list = []

for letter in reversed(input):
	reversed_list.append(letter)
	
print "".join(reversed_list)


