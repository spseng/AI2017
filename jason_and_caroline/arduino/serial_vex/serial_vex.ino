#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
String message;
bool started = false;
int num_count = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (!started) {
    if (Serial.available() > 0) {
      if (Serial.read() == 232) {
        started = true;
        Serial.flush();
      }
    }
  }
  else {
    if (Serial.available() > 0) {
      message = Serial.readStringUntil('\0');
      Serial.flush();
      message.trim();
      if (!(message.length() < 1) && num_count > 0) {
        Serial.println(message);
        lcd.clear();
        lcd.print(message);
      }
      num_count++;
    }
  }
}
