#Have a global variable for the walkMeHome-lights. Boolean
#If its True, let there be light. If False: no light
import time
import comfZone.py
import walkeMeHome.py
import autoBeam.py
import overtake.py
import safeDistance.py
walkeMeHomeLight = True

class Main():

	def drive():
		#Regular drive-state.
		#Run while-loop monitoring speed and distances to cars ahead
		#Keep updated with external methods monitoring safeDistance() + overtake()
		#Terminate loop if gear is put in reverse. Might need more specifications

	def park():
		#Parking-mode
		#While loop: Start sensors that help with parking
		#stop sensors when parking brake is activated.
		#return True, indicating that park is done.
		#Return False if speed > 10 indicating driver will continue driving
		while currentGear == "reverse":
			ComfZone.checkZone()

	def stop():
		timeOn = 60 #maybe add a handler for manual change of time-delay for highbeams?
		if walkMeHome(timeOn, walkMeHomeLight) == 0:
			walkMeHomeLight = False
			return 0
		#run walkMeHome-method
		#get input from a button to determine walkeMeHomeLight's state
		#if RPIO_light_switch == True:
			#walkMeHomeLight = True
		#else:
			#walkMeHomeLight = False	
		#turn on high-beams if global variable is True.
		#Keep them on for a set time, i.e 60 seconds, return 0
		#If False, return 0




def main():
	#controller with a controlVariable set to 1 for online-status
	#run a while loop, keeps running until stop() is done
	#Monitor current car-speed
	#If speed > 0, call drive(). elif gear in reverse, call park.
	#else call the stop method and terminate loop.

	#To finish off, print a goodbye-prompt.

	#Instansiates the needed programs
	comfzone = comfZone.ComfZone()
	autobeam = autoBeam.AutoBeam()
	walkmehome = walkeMeHome.WalkeMeHome()
	over_take = overtake.Overtake()
	safedistance = safeDistance.SafeDistance()

	controll = 1

	while controll == 1:
		currentSpeed = 0
		currentGear = "reverse" #Listens to active changes in gear.
		#Listens to active changes in speed
		if currentSpeed > 10:
			drive()
		elif gear == "reverse": #Reacts only if gear is reverse
			park()
		else:
			stop() #Calls the stop-method. Shall we have a parameter with a timeOn delay?
		if stop() == 0:
			controll = 0


main()