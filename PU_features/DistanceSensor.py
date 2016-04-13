import RPi.GPIO as GPIO
import time
from collections import deque
import statistics
GPIO.setmode(GPIO.BCM)

TRIG_BAK_VENSTRE	 = 26
TRIG_BAK_HOGRE		 = 16
TRIG_FRAMME_VENSTRE	 = 20
TRIG_FRAMME_HOGRE	 = 4
TRIG_FRAMOVER		 = 5


ECHO_BAK_VENSTRE	 = 24 #Connect ECHO to Pin 18 on the Raspberry Pi
ECHO_BAK_HOGRE		 = 23 #Connect ECHO to Pin 40 on the Raspberry Pi
ECHO_FRAMME_VENSTRE	 = 22 #Connect ECHO to Pin 37 on the Raspberry Pi
ECHO_FRAMME_HOGRE	 = 27 #Connect ECHO to Pin 15 on the Raspberry Pi
ECHO_FRAMOVER		 = 6

Lys_Framme_Hogre = 12
Lys_Framme_Venstre =25
Lys_Bak_Hogre = 19
Lys_Bak_Venstre = 13
Lys_Front = 17

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

GPIO.setup(Lys_Framme_Hogre, GPIO.OUT)
GPIO.output(Lys_Framme_Hogre, False)

GPIO.setup(Lys_Framme_Venstre, GPIO.OUT)
GPIO.output(Lys_Framme_Venstre, False)

GPIO.setup(Lys_Bak_Hogre, GPIO.OUT)
GPIO.output(Lys_Bak_Hogre, False)

GPIO.setup(Lys_Bak_Venstre, GPIO.OUT)
GPIO.output(Lys_Bak_Venstre, False)

GPIO.setup(Lys_Front, GPIO.OUT)
GPIO.output(Lys_Front, False)

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
			
			if distance <= 27 and distance > 7:
				GPIO.output(Lys_Bak_Venstre, True)
				time.sleep(distance/200)
				GPIO.output(Lys_Bak_Venstre,False)
			elif distance <= 7 or distance == -1:
				GPIO.output(Lys_Bak_Venstre, True)
			else:
				GPIO.output(Lys_Bak_Venstre, False)

		return distance
	except:
		print("Sensor back left is broken")
		avstand1.append(1)

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
			if distance <= 27.5 and distance >= 7.5:
				GPIO.output(Lys_Framme_Venstre, True)
				time.sleep(distance/200)
				GPIO.output(Lys_Framme_Venstre,False)
			elif distance <= 7.5 or distance == -1:
				GPIO.output(Lys_Framme_Venstre, True)
			else:
				GPIO.output(Lys_Framme_Venstre, False)

		return distance
	except:
		print("Forward left sensor is broken")
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
			if distance <= 30 and distance > 10:
				GPIO.output(Lys_Bak_Hogre, True)
				time.sleep(distance/200)
				GPIO.output(Lys_Bak_Hogre,False)
			elif distance <= 10 or distance == -1:
				GPIO.output(Lys_Bak_Hogre, True)
			else:
				GPIO.output(Lys_Bak_Hogre,False)
			
		return distance
	except:
		print("Sensor back right is broken")
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
			if distance <= 30 and distance >= 10:
				GPIO.output(Lys_Framme_Hogre, True)
				time.sleep(distance/200)
				GPIO.output(Lys_Framme_Hogre,False)
			elif distance <= 10 or distance == -1:
				GPIO.output(Lys_Framme_Hogre, True)
			else:
				GPIO.output(Lys_Framme_Hogre, False)

		return distance
	except:
		print("Sensor forward right is broken")
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
			if distance <= 50:
				GPIO.output(Lys_Front, True)
			else:
				GPIO.output(Lys_Front, False)

			return distance
	except:
		print("Sensor front is broken")
		return -1

def main():
	while(True):
		time.sleep(0.2)
		(bak_venstre())
		(framme_venstre())
		(bak_hogre())
		(framme_hogre())
		(safeDistance())

main()

