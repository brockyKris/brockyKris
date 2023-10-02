/********************************************
* Python file to Log Temperature & Humidity
********************************************/

// import devices?
// import sleep from Time??
// write the calibration of the sensor
// read the sensor
// configure the data to logical output
// write to a log file - sleep for 1 hour for example

// Add baud rate within Serial.begin.
void setup() {
  Serial.begin();
}

// Add sensor position within digitalRead.
void loop() {
  Serial.println(digitalRead()?"HIGH":"LOW");
  delay(200);
}
