#define IN1_2 48
#define IN2_2 49
#define ENA_2 11

void setup() {
  // put your setup code here, to run once:
  /****** Motor 2 setup ******/
  pinMode(IN1_2, OUTPUT);
  pinMode(IN2_2, OUTPUT);
  pinMode(ENA_2, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
    digitalWrite(IN1_2, HIGH);
    digitalWrite(IN2_2, LOW);
  analogWrite(ENA_2, 200);
}
