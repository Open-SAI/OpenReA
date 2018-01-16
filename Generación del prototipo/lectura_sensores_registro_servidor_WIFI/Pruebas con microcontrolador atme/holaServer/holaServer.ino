#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <ESP8266mDNS.h>

const char index_html[]  PROGMEM = {
"<!DOCTYPE html>\n<html>\n<head>\n<style>\nbody {background-color: powderblue;}\nh1   {color: blue;}\np    {color: red;}\nh2 \t {color: black;}\nh6 \t {color: white;}\n</style>\n</head>\n<body>\n<center>\n<h1>OPENSAI ---> Pruebas ESP8266</h1>\n</center>\n<center>\n<h2> Prueba de encendido y apagado de un Led con el m&oacutedulo ESP8266 en Linux </h2>\n\n</center>\n<p>\nOpci&oacuten 1: \n<a href = \"LedOn\"> <button> -- Encender Led -- </button></a>\n<br>\nOpci&oacuten 2: \nLed Apagado\n<br>\nOpci&oacuten 3: \n<a href = \"LedTitila\"> <button> Titila Led </button></a>\n</p>\n<br><br> <br><br> <br><br> <center> <a href=\"http://10.42.0.1\"> <button>INICIO </button></a></center><h6> Diego Alberto Parra Garz&oacuten <br>\nLic. en f&iacutesica <br>\nUniversidad Distrital  <br>\nColombia, Bogot&aacute.\n\n</h6>\n</body>\n</html>"
};

const char Led_Apagado[] PROGMEM = {
  "<!DOCTYPE html>\n<html>\n<head>\n<style>\nbody {background-color: powderblue;}\nh1   {color: blue;}\np    {color: red;}\nh2 \t {color: black;}\nh6 \t {color: white;}\n</style>\n</head>\n<body>\n<center>\n<h1>OPENSAI ---> Pruebas ESP8266</h1>\n</center>\n<center>\n<h2> Prueba de encendido y apagado de un Led con el m&oacutedulo ESP8266 en Linux </h2>\n\n</center>\n<p>\nOpci&oacuten 1: \n<a href = \"LedOn\"> <button> -- Encender Led -- </button></a>\n<br>\nOpci&oacuten 2: \nLed Apagado\n<br>\nOpci&oacuten 3: \n<a href = \"LedTitila\"> <button> Titila Led </button></a>\n</p>\n<br><br> <br><br> <br><br> <center> <a href=\"http://10.42.0.1\"> <button>INICIO </button></a></center><h6> Diego Alberto Parra Garz&oacuten <br>\nLic. en f&iacutesica <br>\nUniversidad Distrital  <br>\nColombia, Bogot&aacute.\n\n</h6>\n</body>\n</html>"
};

const char Led_Encendido[] PROGMEM = {
"<!DOCTYPE html>\n<html>\n<head>\n<style>\nbody {background-color: powderblue;}\nh1   {color: blue;}\np    {color: red;}\nh2 \t {color: black;}\nh6 \t {color: white;}\n</style>\n</head>\n<body>\n<center>\n<h1>OPENSAI ---> Pruebas ESP8266</h1>\n</center>\n<center>\n<h2> Prueba de encendido y apagado de un Led con el m&oacutedulo ESP8266 en Linux </h2>\n\n</center>\n<p>\nOpci&oacuten 1: \nLed Encendido\n<br>\nOpci&oacuten 2: \n<a href = \"LedOff\"> <button> -- Apagar Led -- </button></a>\n<br>\nOpci&oacuten 3: \n<a href = \"LedTitila\"> <button> Titila Led </button></a>\n</p>\n<br><br> <br><br> <br><br> <center> <a href=\"http://10.42.0.1\"> <button>INICIO </button></a></center><h6> Diego Alberto Parra Garz&oacuten <br>\nLic. en f&iacutesica <br>\nUniversidad Distrital  <br>\nColombia, Bogot&aacute.\n\n</h6>\n</body>\n</html>"
};

const char Led_Titilando[] PROGMEM = {
"<!DOCTYPE html>\n<html>\n<head>\n<style>\nbody {background-color: powderblue;}\nh1   {color: blue;}\np    {color: red;}\nh2 \t {color: black;}\nh6 \t {color: white;}\n</style>\n</head>\n<body>\n<center>\n<h1>OPENSAI ---> Pruebas ESP8266</h1>\n</center>\n<center>\n<h2> Prueba de encendido y apagado de un Led con el m&oacutedulo ESP8266 en Linux </h2>\n\n</center>\n<p>\nOpci&oacuten 1: \n<a href = \"LedOn\"> <button> -- Encender Led -- </button></a>\n<br>\nOpci&oacuten 2: \n<a href = \"LedOff\"> <button> -- Apagar Led -- </button></a>\n<br>\nOpci&oacuten 3: \n<a href = \"LedTitila\"> <button> Titila Led </button></a>\n</p>\n<br><br> <br><br> <br><br> <center> <a href=\"http://10.42.0.1\"> <button>INICIO </button></a></center><h6> Diego Alberto Parra Garz&oacuten <br>\nLic. en f&iacutesica <br>\nUniversidad Distrital  <br>\nColombia, Bogot&aacute.\n\n</h6>\n</body>\n</html>"
};

const char* ssid = "Debian-test";
const char* password = "debian123";

ESP8266WebServer server(80);
int EstadoLed;
const int led = 2;

void handleRoot() {
  server.send_P(200, "text/html", index_html);
  digitalWrite(2, LOW);    // turn the LED off by making the voltage LOW    

  digitalWrite(led, 0);

}

void handleNotFound(){
  digitalWrite(led, 1);
  String message = "File Not Found\n\n";
  message += "URI: ";
  message += server.uri();
  message += "\nMethod: ";
  message += (server.method() == HTTP_GET)?"GET":"POST";
  message += "\nArguments: ";
  message += server.args();
  message += "\n";
  for (uint8_t i=0; i<server.args(); i++){
    message += " " + server.argName(i) + ": " + server.arg(i) + "\n";
  }
  server.send(404, "text/plain", message);
  digitalWrite(led, 0);
}

void setup(void){
  pinMode(2, OUTPUT);
  pinMode(led, OUTPUT);
  digitalWrite(led, 0);
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  Serial.println("");

  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(500);                       // wait for a second
    digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
    delay(100);  
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  if (MDNS.begin("esp8266")) {
    Serial.println("MDNS responder started");
  }

  server.on("/", handleRoot);

  server.on("/inline", [](){
    server.send(200, "text/plain", "this works as well");
  });

 server.on("/LedOn", [](){
    server.send_P(200, "text/html", Led_Encendido);
    digitalWrite(2, HIGH);   // turn the LED on (HIGH is the voltage level)
  });

    server.on("/LedOff", [](){
    server.send_P(200, "text/html", Led_Apagado);
    digitalWrite(2, LOW);   // turn the LED on (HIGH is the voltage level)

  });

    server.on("/LedTitila", [](){
    server.send_P(200, "text/html", Led_Titilando);
    for(int i=0; i<=30; i ++)
    {
    digitalWrite(2, LOW);   // turn the LED on (HIGH is the voltage level)
    delay(100);
    digitalWrite(2, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(100);
    }

  });
  
  server.onNotFound(handleNotFound);

  server.begin();
  Serial.println("HTTP server started");
}

void loop(void){
    server.handleClient();
  
   
}

