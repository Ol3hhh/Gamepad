void setup() {
  Serial.begin(9600);
  pinMode(8, INPUT_PULLUP);
  pinMode(25, INPUT_PULLUP);
  for (int pin = 2; pin <= 7; pin++) {
    pinMode(pin, INPUT_PULLUP);
  }
}

void loop() {
  int x1 = analogRead(A0);
  int y1 = analogRead(A1);
  int sw1 = digitalRead(8);

  int x2 = analogRead(A2);
  int y2 = analogRead(A3);
  int sw2 = digitalRead(25);

  int buttons[6];
  for (int i = 0; i < 6; i++) {
    buttons[i] = digitalRead(i + 2);
  }

  Serial.print(x1); Serial.print(",");
  Serial.print(y1); Serial.print(",");
  Serial.print(sw1); Serial.print(",");
  Serial.print(x2); Serial.print(",");
  Serial.print(y2); Serial.print(",");
  Serial.print(sw2); Serial.print(",");
  for (int i = 0; i < 6; i++) {
    Serial.print(buttons[i]);
    if (i < 5) Serial.print(",");
  }
  Serial.println();

  delay(50);
}
