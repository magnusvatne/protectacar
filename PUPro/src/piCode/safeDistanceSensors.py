import RPi.GPIO as GPIO
import time
from collections import deque
import statistics
GPIO.setmode(GPIO.BCM)

TRIG	 = 5
ECHO	 = 6


print ("Distance Measurement In Progress")
#Setup av signal
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG, False)

avstand = deque()

print ("Done setting up, lets go!")

def safeDistance():
	#time.sleep()
	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)
			
	timeoutTime = time.time()
	while GPIO.input(ECHO) == 0:
		pulse_start = time.time()
		if pulse_start - timeoutTime > 3:
			break	

	timeoutTime = time.time()
	while GPIO.input(ECHO) == 1:
		pulse_end = time.time()
		if pulse_end - timeoutTime > 3:
			break

	duration = pulse_end - pulse_start
	distance = duration * 17150
	distance = round(distance,2)
	
	avstand.append(distance)
	if len(avstand) >= 20:
		avstand.popleft()
	distance = round(statistics.median(avstand),2)

	#print (distance, avstand1)
	return distance


def main():
	while(True):
		time.sleep(0.2)
		safeDistance()
main()
