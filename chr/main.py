#Have a global variable for the walkMeHome-lights. Boolean
#If its True, let there be light. If False: no light
import time
import sys
#import comfZone.py
from walkMeHome import walkMeHome
from autobeam import autoMain
#import overtake.py
#import safeDistance.py
from speedMonitor import changeCurrentSpeed
from speedMonitor import deccellerator


#class Main():

def drive(currentSpeed):
	#while (currentSpeed > 10):
	for maintain in range(0,10):
		currentSpeed = changeCurrentSpeed(currentSpeed)
		print('Maintaining: The current speed is: ', currentSpeed)
		time.sleep(0.2)
	for deccelerate in range(0,10):
		currentSpeed = deccellerator(currentSpeed)
		if currentSpeed == 1:
			currentSpeed == 0
			break
		print('Deccelerating: The current speed is: ', currentSpeed)
		time.sleep(0.2)
	print('Deccelerating: The current speed is: ', currentSpeed)

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

	#Will always run when the pi is on.
	#while controll == 1:
	#	currentGear = "reverse" #Listens to active changes in gear.

	#Speeds from 0 to 50. This is a stupid function, but we don't have OBD-II availability
	for accelerate in range (0,20):
	    currentSpeed += 2.5
	    print('The current speed is: ', currentSpeed)
	    time.sleep(0.2)

	#Listens for active changes in speed, changes to drive-state if speed exceeds 10
	if currentSpeed > 10:
		drive(currentSpeed)
	#elif gear == "reverse": WE MIGHT HAVE TO DROP THIS, no OBD-II #Reacts only if gear is reverse
	else:	
		print 'Parking-mode'
		park()
	stop() #Calls the stop-method. Shall we have a parameter with a timeOn delay?

	#This condition checks if the car has stopped. If it has, run the stop-method for walkMeHome



main()