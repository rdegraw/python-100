#--------------------------------------------------
#
# Find the cost to tile a floor 
#
#--------------------------------------------------
import math
	
tile_cost = float( raw_input( "How much does each tile cost? " ))
tile_width = float( raw_input( "How wide is the tile in inches? " ))
tile_length = float( raw_input( "How long is the tile in inches? " ))
floor_width = float( raw_input( "How wide is the floor in inches? " ))
floor_length = float( raw_input( "How long is the floor in inches? " ))

num_tiles_length = math.ceil( floor_length / tile_length )
num_tiles_width = math.ceil( floor_width / tile_width )

total_cost = num_tiles_length * num_tiles_width * tile_cost

print "Your total cost will be %.2f " %total_cost



