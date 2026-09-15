// ESP32 Soil Moisture Sensor

const int sensorPin = 34;   // Analog pin

void setup() {
  Serial.begin(115200);
}

void loop() {

  int sensorValue = analogRead(sensorPin);

  Serial.print("Soil Moisture Value: ");
  Serial.println(sensorValue);

  delay(1000);
}