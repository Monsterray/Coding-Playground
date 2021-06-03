/*
Bluetooth Tracker
Written by Andrew Rohne (arohne@oki.org)
www.oki.org
https://www.siliconcreek.net/transportation/arduino-based-bluetooth-scanners
https://www.sparkfun.com/products/12580
https://www.mouser.com/datasheet/2/268/Class_1_Bluetooth_Module_with_EDR_Support_DS500022-2257897.pdf
*/

#include 
#include 

NewSoftSerial ol(10,11);

char inByte;
boolean ext=false;

void setup(){
  String btreturn;
  Serial.begin(115200);
  delay(1500);
  Serial.print("$$$");
  delay(1000);

}

void loop(){
  byte incomingByte=-1;
  byte index=0;
  char macaddys[160];

  while(Serial.available()>0){
    index=0;
    Serial.println("IN15");
    delay(16500);
    incomingByte=Serial.read();
    while(incomingByte>-1 && index<160){
      macaddys[index]=(char)incomingByte;
      index++;
      incomingByte=Serial.read();
    }
    if(macaddys!=""){
      Serial.end();
      writelog((String)millis()+":"+macaddys+"\r\n");
      Serial.begin(115200);
    }
  }
  if(Serial.available()<=0){
    delay(1000);
    Serial.begin(115200);
  }
    
}

void writelog(String line)
{
  ol.begin(9600);
  ol.print(line);
  ol.end();
}
