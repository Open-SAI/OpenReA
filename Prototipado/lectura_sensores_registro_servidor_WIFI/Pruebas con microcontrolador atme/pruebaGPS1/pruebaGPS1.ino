/*********************
 *10 to GPS Module TX*
 *09 to GPS Module RX*
 *********************/

 /*********************
 *5 to WIFI Module TX*
 *6 to WIFI Module RX*
 *********************/

#include <SoftwareSerial.h>
#include <TinyGPS.h>

SoftwareSerial SerialGPS(10, 11);   //conexión serial con el GPS
SoftwareSerial SerialWIFI(5, 6);  //Conexión y envio de datos al modulo ESP8266

int ValorE;
int tempPin = 0;

TinyGPS gps;

void gpsdump(TinyGPS &gps);

void setup()  
{
  // Oploen serial communications and wait for port to open:
  Serial.begin(9600);
  // set the data rate for the SoftwareSerial port
  SerialGPS.begin(9600);
  delay(1000);
  Serial.println("uBlox Neo 6M");
  Serial.print("Testing TinyGPS library v. ");
  Serial.println(TinyGPS::library_version());
  Serial.println("by Mikal Hart");
  Serial.println();
  Serial.print("Sizeof(gpsobject) = "); 
  Serial.println(sizeof(TinyGPS));
  Serial.println(); 
}

void loop() // run over and over
{
  bool newdata = false;
  unsigned long start = millis();
  // Every 5 seconds we print an update
  while (millis() - start < 5000) 
  {
    if (SerialGPS.available()) 
    
    {
      char c = SerialGPS.read();
      //Serial.print(c);  // uncomment to see raw GPS data
      if (gps.encode(c)) 
      {
        newdata = true;
        break;  // uncomment to print new data immediately!
      }
    }
  }
  
  if (newdata) 
  {
    Serial.println("Datos de Gps Encontrados");
    Serial.println("-------------");
    gpsdump(gps);
    Temperatura();
    Serial.println("-------------");
    Serial.println();
  }
  
}

void gpsdump(TinyGPS &gps)
{
  long lat, lon;
  float flat, flon;
  unsigned long age;

  gps.f_get_position(&flat, &flon, &age);
  Serial.print("Latitud y Longitud: ");
  Serial.print(flat == TinyGPS::GPS_INVALID_F_ANGLE ? 0.0 : flat, 6);
  Serial.print(", ");
  Serial.print(flon == TinyGPS::GPS_INVALID_F_ANGLE ? 0.0 : flon, 6); 
  Serial.print(" Tiempo de procesamiento: ");
  Serial.print(age); Serial.println("ms.");



  // On Arduino, GPS characters may be lost during lengthy Serial.print()
  // On Teensy, Serial prints to USB, which has large output buffering and
  //   runs very fast, so it's not necessary to worry about missing 4800
  //   baud GPS characters.

}

void Temperatura()
{
ValorE = analogRead(tempPin);
float mv = ( ValorE/1024.0)*4500;
float cel = mv/10;
float farh = (cel*9)/5 + 32;

Serial.print("TEMPRATURA \n Celsius:  ");
Serial.print(cel);
Serial.println(" C°");
Serial.print(" \n Farenheit: ");
Serial.print(farh);
Serial.println(" F°");

}


