package piCode;

public class SafeDistance {
	
	
	// should change UI to reflect something
	public boolean checkAhead(double sensorData, double carSpeed){
		return okDistance(sensorData, carSpeed);		
	}
	
	// sensorData is distance to car in front
	private boolean okDistance(double sensorData, double carSpeed){
		
		double carTravelDistance = (carSpeed / 3.6) * 3;
		
		if (sensorData >= carTravelDistance) {
			return true;
		}
		return false;
	}

}
