import RPi.GPIO as GPIO
import time
from collections import deque
GPIO.setmode(GPIO.BCM)

beam = None
lys = 19

GPIO.setup(lys, GPIO.OUT)

class AutoBeam():

	def switchBeam(action):
		global beam
		if action == beam:
			print"Lightstate is already correct"
		elif (beam == False): #This is the method that turns on the highBeam
			beam = True
			GPIO.out(lys, True)
			#Call the method made by Bortne that turns on the lights through RPI
			print('Lights turned on')
		else:
			GPIO.out(lys, False)
			#Call the method made by Bortne that turns off the lights through RPI
			print('Lights turned off')
			beam = False

	def checkThreshold(cameraOutput, threshold):
		#We treat the cameraoutput and compares with threshold. Calls switchBeam with desired action
		treatedValue = treatOutput(cameraOutput)
		if ((treatedValue < threshold) and (beam == False)):
			switchBeam(True)
		elif ((treatedValue > threshold) and (beam == False)):
			switchBeam(False)
		elif ((treatedValue > threshold) and (beam == True)):
			switchBeam(False)
		elif ((treatedValue < threshold) and (beam == True)):
			switchBeam(True)
		else:
			print("Something went wrong with the treated values from the camera-output")

	def treatOutput(cameraOutput):
		#Need to know how the cameraoutputs will be treated before we can code this.
		#What we return so far is simply a float-value
		x = cameraOutput
		x -= 1
		return x

def main(cameraOutput, threshold, lightState):
	#We need to figure out how we want to handle time-delay.
	#It might be a better idea to not have a timed delay here of calling the class,
	#as we won't get updates from this program (camera-updates)
	global beam 
	beam = lightState
	x = 0
	while x < 1:
		if isinstance(cameraOutput, (float)) and isinstance(threshold, (float)):
			checkThreshold(cameraOutput, threshold)
		else:
			print("failerino")
		x += 1

#Test to see if program works
main(8.393, 2.30, True)
main(6.7, 2.30, True)
main(5.2, 2.30, False)
main(0.1, 2.30, False)
main(2.6, 2.30, True)
main(3.0, 2.30, False)