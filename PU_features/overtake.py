import time
from SafeDistance.py import safeDistance()

overtakeDistance = 800.0

def checkOvertake(safeDistance):
	if safeDistance > overtakeDistance:
		print "Overtake OK"
	elif safeDistance < overtakeDistance:
		print "Not safe to overtake"
	else:
		print "ERROR 301" #Sensor cannot determine safe distance
		return 0

def main():

main()