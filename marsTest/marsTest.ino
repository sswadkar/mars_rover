#include <stdio.h>
#include <DS1302.h>
#include <dht.h>

int period = 1000; //time
unsigned long time_now = 0;
int lightVals[100];
int index = 0;
namespace {
const int kCePin   = 5;
const int kIoPin   = 6;
const int kSclkPin = 7;
int sensorPin = A0; 
int lightCal;
DS1302 rtc(kCePin, kIoPin, kSclkPin);
int threshold = 150;
int currentVal;
int rotations;
const int topSpeed = 55; //Since windmills will vary, I used a dyson fan (with a top speed of 55 mph wind speed)
const int topRotations = 26; //max amount of rotations I got with the arduino test was 
float windSpeed;

String dayAsString(const Time::Day day) {
  switch (day) {
    case Time::kSunday: return "Sunday";
    case Time::kMonday: return "Monday";
    case Time::kTuesday: return "Tuesday";
    case Time::kWednesday: return "Wednesday";
    case Time::kThursday: return "Thursday";
    case Time::kFriday: return "Friday";
    case Time::kSaturday: return "Saturday";
  }
  return "(unknown day)";
}
}

dht DHT;
#define DHT11_PIN 8

void setup()
{ 
Serial.begin(9600);
} 
void printTime() {
  // Get the current time and date from the chip.
  Time t = rtc.time();

  // Name the day of the week.
  const String day = dayAsString(t.day);

  // Format the time and date and insert into the temporary buffer.
  char buf[50];
  snprintf(buf, sizeof(buf), "%s %04d-%02d-%02d %02d:%02d:%02d",
           day.c_str(),
           t.yr, t.mon, t.date,
           t.hr, t.min, t.sec);

  // Print the formatted string to serial so we can see the time.
  Serial.print(buf);
  Serial.print(" ");
}
void loop() 
{ 
  lightCal = analogRead(sensorPin); //one measurement every 17.5438596 seconds
  lightVals[index] = lightCal;
  index++;
  if(millis() >= time_now + period){
        time_now += period;
        printTime();
        int chk = DHT.read11(DHT11_PIN);
        Serial.print(DHT.temperature);
        Serial.print(" ");
        Serial.print(DHT.humidity);
        Serial.print(" ");
        currentVal = lightVals[0];
        rotations = 0;
        for(int i = 0; i < 100; i++)
        {
          if (lightVals[i] != 0){
            if ((currentVal - threshold > lightVals[i]) || (currentVal + threshold < lightVals[i])){
              rotations++;
              currentVal = lightVals[i]; 
            }
          }
        }
        windSpeed = topSpeed/topRotations*rotations;
        Serial.println(windSpeed);
        memset(lightVals, 0, sizeof(lightVals));
        index = 0;
    }
    delay(10);
}
