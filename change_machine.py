#--------------------------------------------------
#
# Change Machine 
#   - user enters cost and amount give
#   - we give the proper change back
#
#--------------------------------------------------
import math
dollar = 1
quarter = .25
dime = .10
nickle = .05
penny = .01

cost = float( raw_input( "How much does it cost? ") )
paid = float( raw_input( "How much did you pay? ") )

difference = paid - cost

dollar_change = math.floor(difference)
difference -= dollar_change

quarter_change = math.floor( difference / quarter )
difference = difference % quarter

dime_change = math.floor( difference / dime )
difference = difference % dime

nickle_change = math.floor( difference / nickle )
difference = difference % nickle

penny_change = difference * 100

if dollar_change > 0:
	print int(dollar_change), " dollars"
if quarter_change > 0:
	print int(quarter_change), " quarters"
if dime_change > 0:
	print int(dime_change), " dimes"
if nickle_change > 0:
	print int(nickle_change), " nickles"
if penny_change > 0:
	print int(penny_change), " pennies"





