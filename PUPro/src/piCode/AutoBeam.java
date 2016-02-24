package piCode;

import com.pi4j.io.gpio.GpioController;
import com.pi4j.io.gpio.GpioFactory;
import com.pi4j.io.gpio.GpioPinDigitalOutput;
import com.pi4j.io.gpio.PinState;
import com.pi4j.io.gpio.RaspiPin;

public class AutoBeam {
	boolean lightSwitch = false;
	
	public AutoBeam(double sensorData){
		boolean threshold = checkThreshold(sensorData);
		if (threshold){
			switchBeam();
		}
	}

	private double switchThreshold;

	public void switchBeam(){
		if (!lightSwitch){
			lightSwitch = true;
			pin.toggle();
		}
		else{
			lightSwitch = false;
		}
	}
	
	public boolean checkThreshold(double sensorData){
		if (sensorData > switchThreshold){
			return true;
		}
		return false;
	}
}

public static void main (String args[]){
	// create gpio controller
    final GpioController gpio = GpioFactory.getInstance();
    
    // provision gpio pin #01 as an output pin and turn on
    final GpioPinDigitalOutput pin = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_01, "MyLED", PinState.HIGH);

    // set shutdown state for this pin
    pin.setShutdownOptions(true, PinState.LOW);
}
