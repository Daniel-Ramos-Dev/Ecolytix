const int PIN_MQ = A0;

const int LED_GREEN = 2;
const int LED_YELLOW = 3;
const int LED_RED = 4;

const int LIMIT_GREEN = 300;
const int LIMIT_YELLOW = 450;

const int BUFFER_SIZE = 10;

int readings[BUFFER_SIZE];
int idx = 0;
long sum = 0;
bool filled = false;

void setup() {
  Serial.begin(9600);

  pinMode(LED_GREEN, OUTPUT);
  pinMode(LED_YELLOW, OUTPUT);
  pinMode(LED_RED, OUTPUT);

  for (int i = 0; i < BUFFER_SIZE; i++) {
    readings[i] = 0;
  }
}

void loop() {
  int val = analogRead(PIN_MQ);

  sum -= readings[idx];
  readings[idx] = val;
  sum += val;

  idx = (idx + 1) % BUFFER_SIZE;

  if (idx == 0) {
    filled = true;
  }

  int avg = sum / (filled ? BUFFER_SIZE : idx);

  String status;

  if (avg <= LIMIT_GREEN) {
    status = "GOOD";

    digitalWrite(LED_GREEN, HIGH);
    digitalWrite(LED_YELLOW, LOW);
    digitalWrite(LED_RED, LOW);

  } else if (avg <= LIMIT_YELLOW) {
    status = "MODERATE";

    digitalWrite(LED_GREEN, LOW);
    digitalWrite(LED_YELLOW, HIGH);
    digitalWrite(LED_RED, LOW);

  } else {
    status = "POOR";

    digitalWrite(LED_GREEN, LOW);
    digitalWrite(LED_YELLOW, LOW);
    digitalWrite(LED_RED, HIGH);
  }

  Serial.print(avg);
  Serial.print(",");
  Serial.println(status);

  delay(1000);
}