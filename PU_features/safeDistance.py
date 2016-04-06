import DistanceSensor


class safeDistance:

    # Method called to check if distance to car ahead is acceptable
    def check_ahead(self):
        distance = DistanceSensor.safeDistance()

        if distance < 0:
            return False  # Returns false if sensor is broken
        return self.ok_distance(distance)

    # Method used to calculate the relative distance with the 3 second rule
    def ok_distance(self, sensor_data):
        sensor_data /= 100  # Divided by 100 to accommodate for the sensor monitoring in cm

        car_speed = 60  # TODO Placeholder until car speed can be extracted
        car_travel_distance = (car_speed / 3.6) * 3  # Distance travelled in 3 seconds

        if sensor_data < car_travel_distance:
            return False
        else:
            return True

