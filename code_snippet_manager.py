#------------------------
#
# Code snippet manager
#
#-------------------------
import sys, os, re 
from stat import *


def walktree( top, callback ):

	for f in os.listdir(top):
		pathname = os.path.join(top, f)
		mode = os.stat(pathname)[ST_MODE]
		if S_ISDIR(mode):
			walktree(pathname, callback)
		elif S_ISREG(mode):
			callback(pathname)
		else:
			print 'skipping %s' % pathname

def find_snippets(file):
	if file.endswith('.py'):
		try:
			prog_fl = open( file, 'r' )
		except IOError:
			sys.exit("Could not open file: %s" %file )
		
		def_str = re.compile('^def ')
		print file
		
		for line in prog_fl:
			line = line.strip()
			if def_str.match(line):
				line = line[4:].rstrip(':')
				print "\t",line

		prog_fl.close()

			
		
if __name__ == '__main__':

	script, filename = sys.argv

	walktree(filename, find_snippets)
	
