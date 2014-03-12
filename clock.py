#------------------------
#
# Alarm clock
#	need a good windows graphics lib for 64 - 
#		supposedly pyglet alpha now runs on 64, but need
#       to figure out how to install it as its still tests don't run
#
#-------------------------
from datetime import datetime
import winsound
import time

print datetime.now().time()

#winsound.Beep(30000,10000)
while True:
	print datetime.now().time()
	winsound.MessageBeep()
	time.sleep(10)