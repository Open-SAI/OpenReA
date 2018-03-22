/*
 * --------------------------------------------------------------------------------------------------------------------
 * Example sketch/program showing how to read new NUID from a PICC to serial.
 * --------------------------------------------------------------------------------------------------------------------
 * This is a MFRC522 library example; for further details and other examples see: https://github.com/miguelbalboa/rfid
 * 
 * Example sketch/program showing how to the read data from a PICC (that is: a RFID Tag or Card) using a MFRC522 based RFID
 * Reader on the Arduino SPI interface.
 * 
 * When the Arduino and the MFRC522 module are connected (see the pin layout below), load this sketch into Arduino IDE
 * then verify/compile and upload it. To see the output: use Tools, Serial Monitor of the IDE (hit Ctrl+Shft+M). When
 * you present a PICC (that is: a RFID Tag or Card) at reading distance of the MFRC522 Reader/PCD, the serial output
 * will show the type, and the NUID if a new card has been detected. Note: you may see "Timeout in communication" messages
 * when removing the PICC from reading distance too early.
 * 
 * @license Released into the public domain.
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
 *  esto es softwar libre licnse GPL3
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
    Bluetooth.print("None");
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
