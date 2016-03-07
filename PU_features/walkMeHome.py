import time

class WalkMeHome():

	def walkMeHome(timeOn, walkMeHomeLight):
	       #set highbeams on for timeOn-delay

	       if walkMeHomeLight == 0:
	           return 0
	       else:
	           #run method for turning on autobeam
	           time.sleep(timeOn)
	           #run mehod for turning off autobeam
	           return 1