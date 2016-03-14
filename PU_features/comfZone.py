import DistanceSensor

class ComfZone():
    #Deprecated
    #sensorDataLeft = sensorAccess.get() #placeholder function, should get data
    #sensorDataRight = sensorAccess.get()
    #/Deprecated

    isOn = False #whether ComfZone is turned on by user
    leftPin,rightPin #for giving feedback on whether a car is in your blindzone

    safeDistance = 8#final num to compare with distance from sensor

    def checkZone(): #runs in background, will check zones when isOn = true
        while (isOn):
            sensorDataLeft = DistanceSensor.bak_hogre()
            sensorDataRight = DistanceSensor.bak_venstre()

            #Must implement pin control, unfinished as is
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


    #setter and getter for isOn
    
    def toggleOn(): 
        if (self.isOn)
            self.isOn = False
        self.isOn = True

    def checkOn():
        return self.isOn
