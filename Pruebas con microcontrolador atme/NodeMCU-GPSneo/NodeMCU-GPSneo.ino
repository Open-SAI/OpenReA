#include <TinyGPS.h>

#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <ESP8266mDNS.h>
#include <stdio.h>
#include <string.h>


//#####################################################
// datos ge GPS
/*********************
 *10 to GPS Module TX*
 *11 to GPS Module RX*
 *********************/

#include <SoftwareSerial.h>
#include <TinyGPS.h>



SoftwareSerial SerialGPS(D7, D4 );   //conexión serial con el GPS

int ValorE; //Variable del valor de voltaje por el lm35
int tempPin = A0; //Lectura del PIN A0

  String LatSEND; 
  String LonSEND; 
 String  VelSEND; 
 String TemSEND;
TinyGPS gps;

void gpsdump(TinyGPS &gps);

// ####################################################
// Datos de la red, remplazar según sea el caso
const char* ssid = "Debian-test";
const char* password = "debian123";

// Se crea el LED
const int Led = D5;

// Servidor web en el puerto 80 (por defecto para navegadores)
ESP8266WebServer server(80);

// Se crean las variables para geolocalización y temperatura
int vol=0;

// ###############################################################################################3
// Recordamos que setup() solo se ejecuta el primer ciclo, y es util para configurar puertos y comunicaciones
void setup() 

{
  // Inicializamos el puerto serie a 115200 baudios
  Serial.begin(9600);
  delay(10);
  pinMode(Led, OUTPUT);

  Serial.print("Intentando conectar a ");
  Serial.println(ssid);

  // Nos conectamos al wifi configurado
  WiFi.begin(ssid, password);
  digitalWrite(Led, HIGH);
  while (WiFi.status() != WL_CONNECTED) {
    digitalWrite(Led, LOW);
    delay(250);
    digitalWrite(Led, HIGH);
    delay(250);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("Conexion WiFi establecida");
  
  // Iniciamos el servidor web
  server.begin();
  Serial.println("Por favor, espere a obtener la IP ");
  delay(5000);
  Serial.print("Servidor web online en la IP: ");
  Serial.println(WiFi.localIP());
  digitalWrite(Led, LOW);
    if (MDNS.begin("esp8266")) {
    Serial.println("MDNS responder started");
  }
    server.on("/", []()
    {
      long flat;
      EfectoLed(30);
      server.send(200, "text/html", "<!DOCTYPE html><head>\n<title>formulario</title>\n<meta http-equiv=\"content-type\" content=\"text/html; charset=UTF-8\">\n <meta http-equiv=\"Refresh\" content=\"1; url=http://10.42.0.1/BD/GPS/InsertarGPS.php?Latitud=12&Longitud=123&Temperatura=21&Velocidad=1\"\> <\head><\html>");
      server.send(200, "text/html", TemSEND);

      });

        // Se Inicializa el puerto serial para lectura del GPS
  SerialGPS.begin(9600);
  delay(1000);
}

// funcion de encender y apagar los led con una velocidad determinada
void EfectoLed(int Vel){
  for(int i=0; i<= 3; i++)
  {
  delay(3*Vel);
  digitalWrite(Led, HIGH);
  delay(Vel);
  digitalWrite(Led, LOW);
  delay(Vel);
  }
}

void loop(){
  server.handleClient();
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

    gpsdump(gps);
    Temperatura();

    delay(1000);    

  }

}

void gpsdump(TinyGPS &gps)
{
  long lat, lon;
  float flat, flon;
  unsigned long age;
  gps.f_get_position(&flat, &flon, &age);
 gps.location.lat(); 
  Serial.println("\t LOCALIZACIÓN");
  Serial.print(" Latitud: ");
  Serial.print(flat == TinyGPS::GPS_INVALID_F_ANGLE ? 0.0 : flat, 6);
  Serial.print("° \n Longitud:  ");
  Serial.print(flon == TinyGPS::GPS_INVALID_F_ANGLE ? 0.0 : flon, 6); 
  Serial.print("° \n Tiempo de procesamiento: ");
  Serial.print(age); 

  Serial.print(" ms.\n\n\n");
    
}


void Temperatura()
{
ValorE = analogRead(tempPin);
float mv = ( ValorE/1024.0)*3500;
float cel = mv/10;
float farh = (cel*9)/5 + 32;
Serial.print("\t TEMPERATURA \n Celsius:  ");
Serial.print(cel);
Serial.print(" C°");
Serial.print(" \n Farenheit: ");
Serial.print(farh);
Serial.print(" F°");
Serial.print("\n Kelvin: ");
Serial.print(cel + 273.15);
Serial.print(" K° \n\n\n");

}


