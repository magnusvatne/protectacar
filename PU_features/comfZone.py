import DistanceSensor

class ComfZone():
    #Deprecated
    #sensorDataLeft = sensorAccess.get() #placeholder function, should get data
    #sensorDataRight = sensorAccess.get()
    #/Deprecated


    #PLACEHOLDER VALUES, should be pin for output diode
    bak_venstre_pin = 1
    framme_venstre_pin = 1
    bak_hogre_pin = 1
    framme_hogre_pin = 1


    isOn = False #whether ComfZone is turned on by user
    leftPin,rightPin #for giving feedback on whether a car is in your blindzone

    safeDistance = 8 #final num to compare with distance from sensor

    def checkZone(): #runs in background, will check zones when isOn = true
        while (isOn):
            sensorDataRearLeft = DistanceSensor.bak_hogre()
            sensorDataRearRight = DistanceSensor.bak_venstre()
            sensorDataFrontRight = DistanceSensor.framme_hogre()
            sensorDataFrontLeft = DistanceSensor.framme_venstre()

            if (sensorDataRearLeft < 0 or sensorDataRearRight < 0 or
                sensorDataFrontLeft < 0 or sensorDataFrontRight < 0):
                #do stuff for broken sensor(s)

            if (check(sensorDataRearLeft)):
                DistanceSensor.GPIO.output(bak_venstre_pin, true)
            else:
                DistanceSensor.GPIO.output(bak_venstre_pin, false)

            if (check(sensorDataRearRight)):
                DistanceSensor.GPIO.output(bak_hogre_pin, true)
            else:
                DistanceSensor.GPIO.output(bak_hogre_pin, false)

            if (check(sensorDataFrontLeft)):
                DistanceSensor.GPIO.output(bak_venstre_pin, true)
            else:
                DistanceSensor.GPIO.output(bak_venstre_pin, false)

            if (check(sensorDataFrontLeft)):
                DistanceSensor.GPIO.output(bak_venstre_pin, true)
            else:
                DistanceSensor.GPIO.output(bak_venstre_pin, false)

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
