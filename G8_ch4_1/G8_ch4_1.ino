#include <ESP32Servo.h>

Servo myServo;

int servoPin = 18;

void setup() {
  myServo.attach(servoPin);
}

void loop() {

  // Move to 0°
  myServo.write(0);
  delay(1000);

  // Move to 90°
  myServo.write(90);
  delay(1000);

  // Move to 180°
  myServo.write(180);
  delay(1000);

}