
class main():

	#This method needs to instantly get the current speed of the vehicle via the
	#OBD-II plug from the PI to the car.
	def OBDgetCurrentSpeed():
    """ Gets the speed of the vehicle """
    if self.serialIO is None:
        return "Serial IO not setup."
    self.serialWrite("0D")
    speed_list = self.serialRead()
    if speed_list == -1 or speed_list == 0:
        print("There is an issue with reading the speed of the vehicle.")
        return 0
    else:
        speed_hex = speed_list[1]
        speed_float = float(int("0x" + speed_hex, 0))
        print("Speed float = " + str(speed_float))
        if speedFormat == "mph":
            speed_float = speed_float * 1.609 
        elif speedFormat == "kph":
            return speed_float
        else:
            # error
            print("Configuration is wrong. Please check config.py for speedFormat")
    return speed_float

	def main():
		getCurrentSpeed():

main()