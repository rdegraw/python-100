#--------------------------
#
# Find pi to the nth digit
#
#--------------------------
import math

digits = raw_input( "Please enter the number of digits to calculate PI to: " )

print ('{0:.%df}' % min(20, int(digits))).format(math.pi) # loses precision far before what is printed at 20

#print ('{0:.%df}' % int(digits)).format(4 * (4 * math.atan(1.0/5.0) - math.atan(1.0/239.0))) # machin formula 

