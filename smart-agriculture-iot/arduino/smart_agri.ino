#include <DHT.h>

#define DHTPIN 2
#define DHTTYPE DHT11
#define SOIL_PIN A0

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();
  int soilMoisture = analogRead(SOIL_PIN);

  Serial.print("TEMP:");
  Serial.print(temperature);
  Serial.print(",HUM:");
  Serial.print(humidity);
  Serial.print(",SOIL:");
  Serial.println(soilMoisture);

  delay(5000);
}
