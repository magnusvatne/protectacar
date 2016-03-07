import sensorAccess

class safeDistance:
    def checkAhead(sensorData, carSpeed):
        return okDistance(sensorData,carSpeed)

    def okDistance(sensorData, carSpeed):
    	sensorData = sensorData/100 #Divided by 100 to accomodate for the sensor monitoring in cm
        carTravelDistance = (carSpeed/3.6)*3 #distance travelled in 3 seconds
        if (sensorData < carTravelDistance):
            return false
        return true
