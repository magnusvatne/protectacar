#Have a global variable for the walkMeHome-lights. Boolean
#If its True, let there be light. If False: no light

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

def stop():
	#run walkMeHome-method
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
	controll = 1
	while controll == 1:
		

main()