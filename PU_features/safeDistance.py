import sensorAccess

class safeDistance:
    def checkAhead(sensorData, carSpeed):
        return okDistance(sensorData,carSpeed)

    def okDistance(sensorData, carSpeed):
        carTravelDistance = (carSpeed/3.6)*3 #distance travelled in 3 seconds
        if (sensorData < carTravelDistance):
            return false
        return true
