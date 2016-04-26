import RPi.GPIO as GPIO
import time
from collections import deque
import statistics
GPIO.setmode(GPIO.BCM)

TRIG_BAK_VENSTRE	 = 4
TRIG_BAK_HOGRE		 = 20
TRIG_FRAMME_VENSTRE	 = 16
TRIG_FRAMME_HOGRE	 = 26
TRIG_FRAMOVER		 = 5


ECHO_BAK_VENSTRE	 = 27 #Connect ECHO to Pin 18 on the Raspberry Pi
ECHO_BAK_HOGRE		 = 22 #Connect ECHO to Pin 40 on the Raspberry Pi
ECHO_FRAMME_VENSTRE	 = 23 #Connect ECHO to Pin 37 on the Raspberry Pi
ECHO_FRAMME_HOGRE	 = 24 #Connect ECHO to Pin 15 on the Raspberry Pi
ECHO_FRAMOVER		 = 6


print ("Distance Measurement In Progress")
#Setup av signal
GPIO.setup(TRIG_BAK_VENSTRE, GPIO.OUT)
GPIO.setup(TRIG_BAK_HOGRE, GPIO.OUT)
GPIO.setup(TRIG_FRAMME_VENSTRE, GPIO.OUT)
GPIO.setup(TRIG_FRAMME_HOGRE, GPIO.OUT)
GPIO.setup(TRIG_FRAMOVER, GPIO.OUT)


GPIO.setup(ECHO_BAK_VENSTRE,GPIO.IN)
GPIO.setup(ECHO_BAK_HOGRE,GPIO.IN)
GPIO.setup(ECHO_FRAMME_VENSTRE,GPIO.IN)
GPIO.setup(ECHO_FRAMME_HOGRE,GPIO.IN)
GPIO.setup(ECHO_FRAMOVER, GPIO.IN)

GPIO.output(TRIG_BAK_VENSTRE, False)
GPIO.output(TRIG_BAK_HOGRE, False)
GPIO.output(TRIG_FRAMME_VENSTRE, False)
GPIO.output(TRIG_FRAMME_HOGRE, False)
GPIO.output(TRIG_FRAMOVER, False)

avstand1 = deque()
avstand2 = deque()
avstand3 = deque()
avstand4 = deque()
avstand5 = deque()

print ("Done setting up, lets go!")

def bak_venstre():
	i = 1
	distance = 1
	try: 
		while(i <= 3):
			#time.sleep()
			GPIO.output(TRIG_BAK_VENSTRE, True)
			time.sleep(0.00001)
			GPIO.output(TRIG_BAK_VENSTRE, False)
				
			timeoutTime = time.time()
			while GPIO.input(ECHO_BAK_VENSTRE) == 0:
				pulse_start = time.time()
				if pulse_start - timeoutTime > 3:
					break	
	
			timeoutTime = time.time()
			while GPIO.input(ECHO_BAK_VENSTRE) == 1:
				pulse_end = time.time()
				if pulse_end - timeoutTime > 3:
					break
	
			duration = pulse_end - pulse_start
			distance = duration * 17150
			distance = round(distance,2)
		
			avstand1.append(distance)
			if len(avstand1) >= 10:
				avstand1.popleft()
			distance = round(statistics.median(avstand1),2)
	
			#print (distance, avstand1)
			i += 1
		return distance
	except:
		print("Sensor bak venstre er ødelagt")
		return -1

def framme_venstre():
	i = 1
	distance = 1
	try:
		while(i <= 3):
	                #time.sleep()
			GPIO.output(TRIG_FRAMME_VENSTRE, True)
			time.sleep(0.00001)
			GPIO.output(TRIG_FRAMME_VENSTRE, False)
			
			timeoutTime = time.time()
			while GPIO.input(ECHO_FRAMME_VENSTRE) == 0:
				pulse_start = time.time()
				if pulse_start - timeoutTime > 3:
					break
			
			timeoutTime = time.time()
			while GPIO.input(ECHO_FRAMME_VENSTRE) == 1:
				pulse_end = time.time()
				if pulse_end - timeoutTime > 3:
					break
	
	
			duration = pulse_end - pulse_start
			distance = duration * 17150
			distance = round(distance,2)
	
			avstand2.append(distance)
			if len(avstand2) >= 10:
				avstand2.popleft()
			distance = round(statistics.median(avstand2),2)
	
	                #print (distance, avstand1)
			i += 1
		return distance
	except:
		print("Sensor framme venstre er ødelagt")
		return -1


def bak_hogre():
	i = 1
	distance = 1
	try:
		while(i <= 3):
			GPIO.output(TRIG_BAK_HOGRE, True)
			time.sleep(0.00001)
			GPIO.output(TRIG_BAK_HOGRE, False)
	
			timeoutTime = time.time()
			while GPIO.input(ECHO_BAK_HOGRE) == 0:
				pulse_start = time.time()
				if pulse_start - timeoutTime > 3:
					break
	
			while GPIO.input(ECHO_BAK_HOGRE) == 1:
				pulse_end = time.time()
				if pulse_end - timeoutTime > 3:
					break
	
	
			duration = pulse_end - pulse_start
			distance = duration * 17150
			distance = round(distance,2)
	
			avstand3.append(distance)
			if len(avstand3) >= 10:
				avstand3.popleft()
			distance = round(statistics.median(avstand3),2)
	
	                #print (distance, avstand1)
			i += 1
		return distance
	except:
		print("Sensor bak høgre er ødelagt")
		return -1


def framme_hogre():
	i = 1
	distance = 1
	try:
		while(i <= 3):
			GPIO.output(TRIG_FRAMME_HOGRE, True)
			time.sleep(0.00001)
			GPIO.output(TRIG_FRAMME_HOGRE, False)
			
			timeoutTime = time.time()
			while GPIO.input(ECHO_FRAMME_HOGRE) == 0:
				pulse_start = time.time()
				if pulse_start - timeoutTime > 3:
					break
			
			timeoutTime = time.time()
			while GPIO.input(ECHO_FRAMME_HOGRE) == 1:
				pulse_end = time.time()
				if pulse_end - timeoutTime > 3:
					break
	
			duration = pulse_end - pulse_start
			distance = duration * 17150
			distance = round(distance,2)
	
			avstand4.append(distance)
			if len(avstand4) >= 10:
				avstand4.popleft()
			distance = round(statistics.median(avstand4),2)
	
	                #print (distance, avstand1)
			i += 1
		return distance
	except:
		print("Sensor framme høgre er ødelagt")
		return -1

def safeDistance():
	i = 1
	distance = 1
	try:
		while(True):
			GPIO.output(TRIG_FRAMOVER, True)
			time.sleep(0.00001)
			GPIO.output(TRIG_FRAMOVER, False)
					
			timeoutTime = time.time()
			while GPIO.input(ECHO_FRAMOVER) == 0:
				pulse_start = time.time()
				if pulse_start - timeoutTime > 3:
					break	
		
			timeoutTime = time.time()
			while GPIO.input(ECHO_FRAMOVER) == 1:
				pulse_end = time.time()
				if pulse_end - timeoutTime > 3:
					break
		
			duration = pulse_end - pulse_start
			distance = duration * 17150
			distance = round(distance,2)
			
			avstand5.append(distance)
			if len(avstand5) >= 20:
				avstand5.popleft()
			distance = round(statistics.median(avstand5),2)
		
			#print (distance, avstand1)
			return distance
	except:
		print("Sensor framover er ødelagt")
		return -1

def main():
	while(True):
		time.sleep(1)
		print(bak_venstre())
		print(framme_venstre())
		print(bak_hogre())
		print(framme_hogre())
		print(safeDistance())
		print("")
		print("-----------------")
		print("")

main()
