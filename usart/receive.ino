#arduino mega code
char buffer[6];
void setup() {
  // put your setup code here, to run once:
  Serial1.begin(9600);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial1.available()) {
    Serial1.readBytes(buffer, 1);
    Serial.println(buffer);
  }
  
  delay(1000);
}

#Arduino Uno Code
char buffer[6];
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()) {
    Serial.readBytes(buffer, 1);
    Serial.println(buffer);
  }
  
  delay(1000);
}
