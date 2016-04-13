#Have a global variable for the walkMeHome-lights. Boolean
#If its True, let there be light. If False: no light
import time
import sys
#import comfZone.py
#from walkMeHome import walkMeHome
#from autobeam import autoMain
#import overtake.py
#import safeDistance.py
import threading

from speedMonitor import changeCurrentSpeed
from speedMonitor import deccellerator
from speedMonitor import getGear
#from overtake import checkOvertake
from safeDistance import okDistance
from paparazzi import yetanothermain


def drive(currentSpeed):
#Regular drive-state.
#Running for-loop monitoring speed and distances to cars ahead
#Keep updated with external methods monitoring safeDistance() + overtake()
#Hard-coded deccelerating lets car change state
	thread = threading.Thread(group=None, target=yetanothermain, name=None)
	thread.start()
	for maintain in range(0,10):
		checkOvertake()
		currentSpeed = changeCurrentSpeed(currentSpeed)
		print('Maintaining: The current speed is: ', currentSpeed)
		time.sleep(0.2)
	for deccelerate in range(0,10):
		if not okDistance:
			print 'Slow down asshole!'
		currentSpeed = deccellerator(currentSpeed)
		if currentSpeed == 1:
			currentSpeed == 0
			break
		print('Deccelerating: The current speed is: ', currentSpeed)
		time.sleep(0.2)
	print('Deccelerating: The current speed is: ', currentSpeed)


def park():
#Parking-mode
#While loop that runs while speed is less than 5 or if gear is in reverse.
#return True, indicating that park is done.
#Return False if speed > 10 indicating driver will continue driving
	while (currentGear == "reverse" or currentSpeed < 5):
		currentSpeed = changeCurrentSpeed(currentSpeed)
		currentGear = getGear
		ComfZone.checkZone()
	if currentSpeed > 5:
		drive(currentSpeed)


def stop():
	#This method is called when driver has stopped.
	#It asks for user input to determine if user wants the walkMeHome-function,
	#and if so, how long it will be on
	default = 'yes'
	valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}

	print 'Car stopped, calling walkMeHome-function'
	if default is None:
		prompt = " [y/n] "
	elif default == "yes":
		prompt = " [Y/n] "
	elif default == "no":
		prompt = " [y/N] "
	else:
		raise ValueError("invalid default answer: '%s'" % default)

	while True:        
		sys.stdout.write('Would you like to keep highbeams on? ' + prompt)
		choice = raw_input().lower()
		if default is not None and choice == '':
			return valid[default]
		elif choice in valid:
			return valid[choice]
		else:
			sys.stdout.write("Please respond with 'yes' or 'no' "
			"(or 'y' or 'n').\n")
		if valid:
			print 'How long would you like the lights on(answer in seconds)? '
			walkMeHome(timeOn)
		print 'Good bye'
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

	#Instansiates the needed variables and programs
	walkMeHomeLight = True
	currentSpeed = 0
	controll = 1

	#Speeds from 0 to 50. This is a stupid function, but we don't have OBD-II availability
	for accelerate in range (0,20):
	    currentSpeed += 2.5
	    print('The current speed is: ', currentSpeed)
	    time.sleep(0.2)

	#Listens for active changes in speed, changes to drive-state if speed exceeds 10
	if currentSpeed > 10:
		drive(currentSpeed)
	#elif gear == "reverse": WE MIGHT HAVE TO DROP THIS, no OBD-II #Reacts only if gear is reverse
	print 'Parking-mode'
	park()

	print 'Stop-mode'
	stop() #Calls the stop-method. Shall we have a parameter with a timeOn delay?

	#This condition checks if the car has stopped. If it has, run the stop-method for walkMeHome



main()