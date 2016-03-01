package piCode;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.nio.charset.Charset;
import java.nio.file.Files;

import com.pi4j.io.gpio.GpioController;
import com.pi4j.io.gpio.GpioFactory;
import com.pi4j.io.gpio.GpioPinDigitalOutput;
import com.pi4j.io.gpio.PinState;
import com.pi4j.io.gpio.RaspiPin;
import java.util.EventListener;
import java.util.Scanner;

import javafx.beans.value.ObservableValue;

import javax.swing.event.ChangeEvent;
//import java.util.EventListener;

public class AutoBeam {
	boolean on;
	boolean lightSwitch = false;
	boolean cameraOutput;
	
	BufferedReader reader = null;
	
	public ChangeListener cameraChange = new ChangeListener<ChangeListener>();
	
	
	
	public AutoBeam(double sensorData){
		boolean threshold = checkThreshold(sensorData);
		while (on==true && cameraOutput == true){
			if (threshold){
				switchBeam();
			}
			continue;
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
			pin.toggle();
		}
	}
	
	public boolean checkThreshold(double sensorData){
		if (sensorData > switchThreshold){
			return true;
		}
		return false;
	}
	
	void addChangeListener(ChangeListener changedCameraOutput){
		
	}

public static void main (String args[]){
	File cameraFile = new File("cameraoutput.txt");
	
	// create gpio controller
    //final GpioController gpio = GpioFactory.getInstance();
    
    // provision gpio pin #01 as an output pin and turn on
    //final GpioPinDigitalOutput pin = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_01, "MyLED", PinState.HIGH);

    // set shutdown state for this pin
    //pin.setShutdownOptions(true, PinState.LOW);
    
    try{
    	Scanner input = new Scanner(cameraFile);
    	while (input.hasNext()){
    		String cameraValue = input.nextLine();
    		System.out.println("CameraFile has been read.");
    	}
    }
    
    catch(FileNotFoundException e){
    	System.err.format("File does not exist");
    }
	}
    
   
}
