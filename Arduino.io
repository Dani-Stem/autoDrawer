#include <Servo.h>


Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards


int pos = 180;	// variable to store the servo position


void setup() {
 myservo.attach(9);
 Serial.begin(9600);


}

void loop() {
	if (Serial.available() > 0) {
    	String data = Serial.readStringUntil('\n');
    	data.trim();
    	Serial.println("Received: " + data);

    	if (data == "open") {
        	for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
            	// in steps of 1 degree
            	myservo.write(pos);          	// tell servo to go to position in variable 'pos'
            	delay(15);                   	// waits 15ms for the servo to reach the position
        	}
    	} else if (data == "close") {
        	for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
            	myservo.write(pos);          	// tell servo to go to position in variable 'pos'
            	delay(15);                   	// waits 15ms for the servo to reach the position
        	}
    	} else {
        	Serial.println("Bad data: "  + data);
    	}
	}
    
}






