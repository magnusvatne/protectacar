import sensorAccess

class ComfZone():
    sensorDataLeft = sensorAccess.get() #placeholder function, should get data
    sensorDataRight = sensorAccess.get()
    isOn = False #whether ComfZone is turned on by user
    leftPin,rightPin #for giving feedback on whether a car is in your blindzone

    safeDistance = 8#final num to compare with distance from sensor

    def checkZone():
        while (isON):
            sensorDataLeft = sensorAccess.get()
            sensorDataRight = sensorAccess.get()

            if (check(sensorDataLeft)):
                leftPin.toggleOn
            else:
                leftPin.toggleOff

            if (check(sensorDataRight)):
                rightPin.toggleOn
            else:
                rightPin.toggleOff


    def check(sensorData):
        if (sensorData < safeDistance):
            return true
        return false

    def setOn(on):
        self.isOn = on
