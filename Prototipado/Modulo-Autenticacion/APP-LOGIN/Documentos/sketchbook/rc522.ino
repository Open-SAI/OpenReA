/*
 * --------------------------------------------------------------------------------------------------------------------
 * 
 * Typical pin layout used:
 * -----------------------------------------------------------------------------------------
 *             MFRC522      Arduino       Arduino   Arduino    Arduino          Arduino
 *             Reader/PCD   Uno/101       Mega      Nano v3    Leonardo/Micro   Pro Micro
 * Signal      Pin          Pin           Pin       Pin        Pin              Pin
 * -----------------------------------------------------------------------------------------
 * RST/Reset   RST          9             5         D9         RESET/ICSP-5     RST
 * SPI SS      SDA(SS)      10            53        D10        10               10
 * SPI MOSI    MOSI         11 / ICSP-4   51        D11        ICSP-4           16
 * SPI MISO    MISO         12 / ICSP-1   50        D12        ICSP-1           14
 * SPI SCK     SCK          13 / ICSP-3   52        D13        ICSP-3           15
 * 
 *  
 *  
 *  DIEGO ALBERTO PARRA GARZÓN, MODIFIQUE EL SCRIPT AÑADIENDO UN MENÚ Y DANDOLE 
 *  SALIDA A LA COMUNICACIÓN BLUETOOTH
 *  esto es softwar libre license GPL3
 *  
 * PINES BLUETOOTH 
 * SIGNAL  PIN
 *   RX     3
 *   TX     4
 */

#include <SPI.h>
#include <MFRC522.h>
#include <SoftwareSerial.h>

#define SS_PIN 10
#define RST_PIN 9
#define Rx 3
#define Tx 4

SoftwareSerial Bluetooth(Tx, Rx);

MFRC522 rfid(SS_PIN, RST_PIN); // Instance of the class

MFRC522::MIFARE_Key key; 

// Init array that will store new NUID 
byte nuidPICC[4];

void setup() { 
  Bluetooth.begin(9600);
  Serial.begin(9600);
  SPI.begin(); // Init SPI bus
  rfid.PCD_Init(); // Init MFRC522 
}


void RevisarTarjetas()
{
  bool option1 = rfid.PICC_IsNewCardPresent();
//  Bluetooth.println(option1);
  Serial.println("Revisando si hay tarjetas ...");  
  if(option1==0)
  {
    Serial.println("No se encontro ningúna tarjeta, por favor acerque su tarjeta al dispositivo ... ");
    Serial.println("\r\n");
    Bluetooth.print("Nada");
    Bluetooth.print("\r\n");
  }
  if  (option1!=0)
  {
    Serial.println("\n Se encontro un dispositivo ....");
    Serial.println("Su NUID es: ");
    rfid.PICC_ReadCardSerial();
     // Store NUID into nuidPICC array
    for (byte i = 0; i < 4; i++) 
    {
      nuidPICC[i] = rfid.uid.uidByte[i];
    }
    ValorHex(rfid.uid.uidByte, rfid.uid.size);
    Serial.println("\r\n");
    Bluetooth.print("\r\n");

  }
}



void ValorHex(byte *buffer, byte bufferSize) {
  for (byte i = 0; i < bufferSize; i++) {
    Bluetooth.print(buffer[i] < 0x10 ? " 0" : " ");
    Bluetooth.print(buffer[i], HEX);    
    Serial.print(buffer[i] < 0x10 ? " 0" : " ");
    Serial.print(buffer[i], HEX);    
  }
}

void ValorDec(byte *buffer, byte bufferSize) {
  for (byte i = 0; i < bufferSize; i++) {
    Serial.print(buffer[i] < 0x10 ? " 0" : " ");
    Serial.print(buffer[i], DEC);
    Bluetooth.print(buffer[i] < 0x10 ? " 0" : " ");
    Bluetooth.print(buffer[i], DEC);
    
  }
}

 
void Menu()
{
  
  char opcion = Bluetooth.read();
//  char opcion = Serial.read();
  
  switch (opcion )
  {
    case 'a':
                Serial.println("Opción 1, activada");
                RevisarTarjetas();
                Serial.println("Opción 1, desactivada, llamando al menú.");
                Menu();                              
              break;
   }
}

void loop()
{
  
  Menu();
    
}