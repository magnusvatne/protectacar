#Have a global variable for the walkMeHome-lights. Boolean
#If its True, let there be light. If False: no light
import time
#import comfZone.py
from walkMeHome import walkMeHome
#import autoBeam.py
#import overtake.py
#import safeDistance.py
from speedMonitor import changeCurrentSpeed


#class Main():

def drive(currentSpeed):
	while (currentSpeed > 10):
		currentSpeed = changeCurrentSpeed(currentSpeed)
		print('The current speed is: ', currentSpeed)
		time.sleep(0.5)
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
	while (currentGear == "reverse" and currentSpeed < 10):
		ComfZone.checkZone()
	if currentGear != "reverse":
		currentGear = 0

def stop(walkMeHomeLight):
	timeOn = 60 #maybe add a handler for manual change of time-delay for highbeams?
	if walkMeHome(timeOn, walkMeHomeLight) == 0:
		walkMeHomeLight = False
		return 0
	return -1
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
	#comfzone = comfZone.ComfZone()
	#autobeam = autoBeam.AutoBeam()
	#over_take = overtake.Overtake()
	#safedistance = safeDistance.SafeDistance()
	walkMeHomeLight = True
	currentSpeed = 0
	controll = 1

	#Will always run when the pi is on.
	#while controll == 1:
	#	currentGear = "reverse" #Listens to active changes in gear.

	#Speeds from 0 to 50. This is a stupid function, but we don't have OBD-II
	for i in range (0,20):
	    currentSpeed += 2.5
		#time.sleep(0.2)

	#Listens for active changes in speed, changes to drive-state if speed exceeds 10
	if currentSpeed > 10:
		drive(currentSpeed)
	elif gear == "reverse": #Reacts only if gear is reverse
		park()
	else:
		stop() #Calls the stop-method. Shall we have a parameter with a timeOn delay?

	#This condition checks if the car has stopped. If it has, run the stop-method for walkMeHome
	if stop(walkMeHomeLight) == 0:
		controll = 0



main()