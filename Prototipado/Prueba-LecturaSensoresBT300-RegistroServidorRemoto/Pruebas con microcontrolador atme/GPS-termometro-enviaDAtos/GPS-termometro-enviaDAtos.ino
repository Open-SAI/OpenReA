/*********************
 *10 to GPS Module TX*
 *11 to GPS Module RX*
 *********************/

#include <SoftwareSerial.h>
#include <TinyGPS.h>

//Tx al 10; Rx al 11
SoftwareSerial SerialGPS(10, 11);   //conexión serial con el GPS

int ValorE; //Variable del valor de voltaje por el lm35
int tempPin = A0; //Lectura del PIN A0

const int Led1 = 4;
 const int Led2 = 2;

TinyGPS gps;

void gpsdump(TinyGPS &gps);



void setup()  
{
  // Se inicializa el puerto serial para comunicación con el ESP8266
  Serial.begin(9600);
  pinMode(Led1, OUTPUT);
  pinMode(Led2, OUTPUT);
  // Se Inicializa el puerto serial para lectura del GPS
  SerialGPS.begin(9600);
  EfectoLed(50);

/*
  Serial.println("uBlox Neo 6M");
  Serial.print("Testing TinyGPS library v. ");
  Serial.println(TinyGPS::library_version());
  Serial.println("by Mikal Hart");
  Serial.println();
  Serial.print("Sizeof(gpsobject) = "); 
  Serial.println(sizeof(TinyGPS));
  Serial.println(); */
}

void loop() // run over and over
{
  EfectoLed(10);
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
    /*
    Serial.println("Datos de Gps Encontrados");
    Serial.println("-------------");*/
    gpsdump(gps);
    Temperatura();
    EfectoLed(130);
    Serial.println();
  }
  
}

void gpsdump(TinyGPS &gps)
{
  long lat, lon;
  float flat, flon;
  unsigned long age;

  gps.f_get_position(&flat, &flon, &age);
 // Serial.print("Latitud y Longitud: ");
  Serial.print("A");
  Serial.print(flat == TinyGPS::GPS_INVALID_F_ANGLE ? 0.0 : flat, 6);
  Serial.print("A");
  Serial.print(flon == TinyGPS::GPS_INVALID_F_ANGLE ? 0.0 : flon, 6); 
  Serial.print("A");
  //Serial.print("\n Tiempo de procesamiento: ");
  Serial.print(age); //Serial.print("ms.\n");
  Serial.print("A");
  
}


void Temperatura()
{
ValorE = analogRead(tempPin);
float mv = ( ValorE/1024.0)*5000;
float cel = mv/100;
float farh = (cel*9)/5 + 32;

//Serial.print("\t TEMPERATURA \n Celsius:  ");

Serial.print(cel);
//Serial.print("A");
Serial.print("\r \n");
/*Serial.println(" C°");
Serial.print(" \n Farenheit: ");
Serial.print(farh);
Serial.println(" F°");
*/
}


void EfectoLed(int VeLed)
{
   for (int i = 0; i<=5; i++)
   {
    digitalWrite(Led1, HIGH);
    delay(VeLed);
    digitalWrite(Led1, LOW);
    delay(VeLed);
    digitalWrite(Led2, HIGH);
    delay(VeLed);
    digitalWrite(Led2, LOW);
    delay(VeLed);
   }
}

