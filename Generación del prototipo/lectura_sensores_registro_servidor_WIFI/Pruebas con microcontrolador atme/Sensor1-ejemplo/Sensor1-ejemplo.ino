int sensorValue = 0;  // variable to store the value coming from the sensor
int sensorPin = A1; 

void setup() {
  Serial.begin(9600);
  pinMode(2, OUTPUT);
  pinMode(4, OUTPUT);
    pinMode(sensorPin, INPUT);

}

void loop() { 
  digitalWrite(4, HIGH);   
  float PPM = analogRead(sensorPin);
  PPM = 100*PPM/1023*5;
//  digitalWrite(4, LOW);
  Serial.print(PPM);
  digitalWrite(2, HIGH);
  delay(1600);
  digitalWrite(2, LOW);
  delay(1600);
  Serial.print("\r\n");
}
