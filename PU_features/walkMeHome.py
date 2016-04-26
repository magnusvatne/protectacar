import time
from autoBeam import switchBeam

def walkMeHome(timeOn):
  #set highbeams on for timeOn-delay
      #run method for turning on autobeam
      switchBeam(True)
      #Wait the given amount of time
      time.sleep(timeOn)
      #run mehod for turning off autobeam
      switchBeam(False)