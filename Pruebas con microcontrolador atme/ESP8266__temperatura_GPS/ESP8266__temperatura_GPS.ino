#include <ESP8266WiFi.h>
#include <stdio.h>
#include <string.h>

// Replace with your network details
const char* ssid = "Debian-test";
const char* password = "debian123";

// Servidor web en el puerto 80 (por defecto para navegadores)
WiFiServer server(80);

// Pin del sensor DHT, en mi caso GPI02
const int DHTPin = 2;
const int DHTPin1 = 0;
int vol=0;
String vol1="";
String Latitud="";
String Longitud="";
String VeTrans="";
String Temperatura="";

// Recordamos que setup() solo se ejecuta el primer ciclo, y es util para configurar puertos y comunicaciones
void setup() 

{
  // Inicializamos el puerto serie a 115200 baudios
  Serial.begin(9600);
  delay(10);
  pinMode(DHTPin, INPUT);
  Serial.println();
  Serial.print("Intentando conectar a ");
  Serial.println(ssid);

  // Nos conectamos al wifi configurado
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
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
}


String  DECtoACII(int valor)
{
  String conversion;
  if (valor == 45)
  {
    conversion = "-";
  }

    if (valor == 46)
  {
    conversion = ".";
  }

    if (valor == 44)
  {
    conversion = ",";
  }

 if (valor == 48)
  {
    conversion = "0";
  }
   if (valor == 49)
  {
    conversion = "1";
  }
   if (valor == 50)
  {
    conversion = "2";
  }
   if (valor == 51)
  {
    conversion = "3";
  }
   if (valor == 52)
  {
    conversion = "4";
  }
   if (valor == 53)
  {
    conversion = "5";
  }
   if (valor == 54)
  {
    conversion = "6";
  }
   if (valor == 55)
  {
    conversion = "7";
  }
   if (valor == 56)
  {
    conversion = "8";
  }
   if (valor == 57)
  {
    conversion = "9";
  }

    if (valor == 65)
  {
    conversion = ":";
  }

  return conversion;
}

void loop() {
  digitalWrite(DHTPin1, HIGH);   // turn the LED on (HIGH is the voltage level)
  // Esperamos nuevo cliente

  WiFiClient client = server.available();
  
  if (client) {    
    Serial.println("Nuevo cliente");
    boolean blank_line = true;
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();

        if (c == '\n' && blank_line) {
            // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
            String vol2="";

             while (Serial.available() > 0) {               
                vol = Serial.read(); 
                vol1 = DECtoACII(vol);
                if (vol1 != "\n")
                {         
                  // say what you got:
                Serial.print("I received: ");
                Serial.println(vol1);
                vol2 += vol1;  
                }
                
            }
            Latitud = getValue(vol2, ':', 1);
            Longitud=getValue(vol2, ':', 2);
            VeTrans=getValue(vol2, ':', 3);
            Temperatura=getValue(vol2, ':', 4);
 /*           Serial.println(Latitud);
            Serial.println(Longitud);
            Serial.println(VeTrans);
            Serial.println(Temperatura);
*/
            //Latitud = getValue(vol2, ':', 0);
            
            if (Latitud != " ")
          {
            client.println("HTTP/1.1 200 OK");
            client.println("Content-Type: text/html");
            client.println("Connection: close");
            client.println();
            client.println("<!DOCTYPE HTML>");
            client.println("<html>");
            client.println("<head>\n<title>formulario</title>\n<meta http-equiv=\"content-type\" content=\"text/html; charset=UTF-8\">\n <meta http-equiv=\"Refresh\" content=\"2; url=http://10.42.0.1/BD/GPS/InsertarGPS.php?Latitud=");
            client.print(Latitud);
            client.print("&Longitud=");            
            client.print(Longitud);
            client.print("&Temperatura=");
            client.print(Temperatura);
            client.print("&Velocidad=");                        
            client.print(VeTrans);
            client.print("\">  </head>\n\n<body>");
            client.println("Enviando dats");            
            client.println("</body></html>");     
            break;
          }
        }
        if (c == '\n') {
          // when starts reading a new line
          blank_line = true;
        }
        else if (c != '\r') {
          // when finds a character on the current line
          blank_line = false;
        }
      }
    }  
    // Cerrando conexión con el cliente
    delay(1);
    client.stop();
    Serial.println("Cliente desconectado.");
    digitalWrite(DHTPin1, HIGH);   // turn the LED on (HIGH is the voltage level)
    
  }
}   


 String getValue(String data, char separator, int index)
{
  int found = 0;
  int strIndex[] = {0, -1};
  int maxIndex = data.length()-1;

  for(int i=0; i<=maxIndex && found<=index; i++){
    if(data.charAt(i)==separator || i==maxIndex){
        found++;
        strIndex[0] = strIndex[1]+1;
        strIndex[1] = (i == maxIndex) ? i+1 : i;
    }
  }

  return found>index ? data.substring(strIndex[0], strIndex[1]) : "";
}


                       

            
