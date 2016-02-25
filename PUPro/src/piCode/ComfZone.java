package piCode;

import sensorAccess;

public class ComfZone {
	
	private Pin rightPin;
	private Pin lefPin;
	private boolean on;
	private double sensorDataLeft;
	private double sensorDataRight;
	
	public final double safeDistance = 2; 
	
	public void checkZone(){
		
		// placeholder
		sensorDataLeft = getSensorData();
		sensorDataRight = getSensorData();
		
		while (on==true){
			if (checkLeft(sensorDataLeft)) {
				leftPin.toggleOn; //placeholder
			} else {
				leftPin.toggleOff;
			}
			
			if (checkRight(sensorDataRight)) {
				rightPin.toggleOn;
			} else {
				rightPin.toggleOff;
			}
		}
		
	}
	
	private boolean checkLeft(double sensorData) {
		if (sensorData < safeDistance) {
			return true;
		}
		return false;
	}

	private boolean checkRight(double sensorData) {
		if (sensorData < safeDistance) {
			return true;
		}
		return false;
	}
	
	public boolean isOn() {
		return on;
	}

	public void setOn(boolean on) {
		this.on = on;
	}
	
	public static void main(String[]args){
		//Main-method
	}
	
}