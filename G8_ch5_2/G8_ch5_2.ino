const int sensorPin = 34;

void setup() {
  Serial.begin(115200);
}

void loop() {

  int sensorValue = analogRead(sensorPin);

  // Convert sensor value to percentage
  // Adjust 3500 and 1200 after calibration
  int moisture = map(sensorValue, 3500, 1200, 0, 100);

  // Keep value between 0 and 100
  moisture = constrain(moisture, 0, 100);

  Serial.print("Sensor Value: ");
  Serial.print(sensorValue);

  Serial.print("   Moisture: ");
  Serial.print(moisture);
  Serial.println("%");

  delay(1000);
}