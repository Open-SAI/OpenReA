/*
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
 */



 /*********************
 *5 to GPS Module TX*
 *6 to GPS Module RX*
 *********************/
 
#include <SoftwareSerial.h>
#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN         9
#define SS_PIN          10
MFRC522 mfrc522(SS_PIN, RST_PIN);

#define RxD 6   // DEFINO EL RX DEL BLUETOOTH
#define TxD 7   //DEFINO EL TX DEL BLUETOOTH

SoftwareSerial Blue(TxD, RxD);

void setup()
{
   Serial.begin(9600);
   Blue.begin(9600);
   SPI.begin();
   mfrc522.PCD_Init();
 }

void loop() 
{
  RfidScan();
}

void dump_byte_array(byte *buffer, byte bufferSize) 
{
 for (byte i = 0; i < bufferSize; i++) 
 {
   //Serial.print(buffer[i] < 0x10 ? ” 0″ : ”“);
   Serial.print(buffer[i], HEX);
   Blue.print(buffer[i], HEX);
 }
 Serial.println("\n");
 Blue.print("\r\n");
}

void RfidScan()
{
  if ( ! mfrc522.PICC_IsNewCardPresent())
  return;

  if ( ! mfrc522.PICC_ReadCardSerial())
  return;
  dump_byte_array(mfrc522.uid.uidByte, mfrc522.uid.size);
  }
