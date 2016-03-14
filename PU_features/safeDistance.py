import DistanceSensor

class safeDistance:

        carSpeed = 60 #Placeholder until car speed can be extracted

	def checkAhead():
            distance = DistanceSensor.safeDistance()
            if (distance < 0)
                    return False #returns false if sensor is broken
	    return okDistance(distance,carSpeed) 

	def okDistance(sensorData, carSpeed):
            sensorData = sensorData/100 #Divided by 100 to accomodate for the sensor monitoring in cm
	    carTravelDistance = (carSpeed/3.6)*3 #distance travelled in 3 seconds
	    if (sensorData < carTravelDistance):
	        return False
	    return True
