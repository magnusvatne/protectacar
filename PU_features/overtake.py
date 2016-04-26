import DistanceSensor


class Overtake:

    # PLACEHOLDER VALUE, should be pin for output diode
    overtake_pin = 1

    isOn = True  # Whether comfort zone is turned on by user
    overtake_distance = 800.0  # Final num to compare with distance from sensor

    def check_overtake(self):
        distance = DistanceSensor.safeDistance()

        if distance < 0:
            return False  # Returns false if sensor is broken
        return self.ok_distance(distance)

    # Method used to calculate the distance acceptable to use for overtaking car in front
    def ok_distance(self, sensor_data):
        sensor_data /= 100  # Divided by 100 to accommodate for the sensor monitoring in cm

        car_speed = 60  # TODO Placeholder until car speed can be extracted

        car_travel_distance = (car_speed / 3.6) * 3  # Distance travelled in 3 seconds

        if sensor_data < car_travel_distance:
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


def main():
    Overtake.check_overtake()

main()
