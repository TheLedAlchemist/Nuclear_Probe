const int diodePin = 0;
const int ledPin = 13;

void setup() {
  // put your setup code here, to run once:
  
  // Configure I/O and initialize serial connection to 9.6k
  pinMode(diodePin, INPUT);
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int lightValue = analogRead(diodePin);  // Read the state of the photodiode pin

  Serial.println(lightValue);

  delay(100);  // Delay for 100 ms before reading again (adjust as needed)

}
