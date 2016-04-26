import DistanceSensor


class ComfZone:

    # PLACEHOLDER VALUES, should be pin for output diode
    rear_left_pin = 1
    front_left_pin = 1
    rear_right_pin = 1
    front_right_pin = 1

    isOn = True  # Whether comfort zone is turned on by user
    safe_distance = 8  # Final num to compare with distance from sensor

    def check_zone(self):  # Runs in background, will check zones when isOn = true
        if self.isOn:
            sensdata_rearleft = DistanceSensor.bak_venstre()
            sensdata_rearright = DistanceSensor.bak_hogre()
            sensdata_frontleft = DistanceSensor.framme_venstre()
            sensdata_frontright = DistanceSensor.framme_hogre()

            if sensdata_rearleft < 0 or sensdata_rearright < 0 or sensdata_frontright < 0 or sensdata_frontleft < 0:
                # TODO do stuff with broken sensor
                return False  # Placeholder

            if self.ok_distance(sensdata_rearleft):
                DistanceSensor.GPIO.output(self.rear_left_pin, True)
            else:
                DistanceSensor.GPIO.output(self.rear_left_pin, False)

            if self.ok_distance(sensdata_rearright):
                DistanceSensor.GPIO.output(self.rear_right_pin, True)
            else:
                DistanceSensor.GPIO.output(self.rear_right_pin, False)

            if self.ok_distance(sensdata_frontright):
                DistanceSensor.GPIO.output(self.rear_left_pin, True)
            else:
                DistanceSensor.GPIO.output(self.rear_left_pin, False)

            if self.ok_distance(sensdata_frontright):
                DistanceSensor.GPIO.output(self.rear_left_pin, True)
            else:
                DistanceSensor.GPIO.output(self.rear_left_pin, False)

    # Method used to determine if distance to cars in the comfort zone is ok
    def ok_distance(self, sensor_data):
        sensor_data /= 100  # Divided by 100 to accommodate for the sensor monitoring in cm

        if sensor_data < self.safe_distance:
            return False
        else:
            return True

    # Setter and getter for isOn
    def toggle_on(self):
        if self.isOn:
            self.isOn = False
        self.isOn = True

    def check_on(self):
        return self.isOn
