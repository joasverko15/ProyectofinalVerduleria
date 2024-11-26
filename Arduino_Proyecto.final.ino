#include <SPI.h>
#include <MFRC522.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>


#define RST_PIN         9
#define SS_PIN          10
#define LED_ROJO_PIN    7
#define LED_AZUL_PIN    6

MFRC522 mfrc522(SS_PIN, RST_PIN); 
LiquidCrystal_I2C lcd(0x27, 16, 2); 
 
byte desiredUID[] = {0x43, 0x6F, 0x27, 0x16};


float saldo = 100.0; 
const float COSTO = 10.0; 

void setup() {
    Serial.begin(9600);  
    while (!Serial);

    
    SPI.begin();
    mfrc522.PCD_Init();

    
    pinMode(LED_ROJO_PIN, OUTPUT);
    pinMode(LED_AZUL_PIN, OUTPUT);
    digitalWrite(LED_ROJO_PIN, LOW);
    digitalWrite(LED_AZUL_PIN, LOW);

    
    lcd.init();
    lcd.backlight();
    lcd.setCursor(0, 0);
}

void loop() {
    
    if (!mfrc522.PICC_IsNewCardPresent()) {
        return;
    }

    
    if (!mfrc522.PICC_ReadCardSerial()) {
        return;
    }

    
    Serial.print("UID de la tarjeta: ");
    for (byte i = 0; i < mfrc522.uid.size; i++) {
        Serial.print(mfrc522.uid.uidByte[i], HEX);
        Serial.print(" ");
    }
    Serial.println();

   
    if (compareUID(mfrc522.uid.uidByte, desiredUID, mfrc522.uid.size)) {
        if (saldo >= COSTO) {
             saldo -= COSTO; 
            Serial.println("Transacción exitosa.");
            Serial.print("Nuevo saldo: ");
            Serial.println(saldo);

            digitalWrite(LED_AZUL_PIN, HIGH);
            digitalWrite(LED_ROJO_PIN, LOW);

            
            lcd.clear();
            lcd.setCursor(0, 0);
            lcd.print("Transaccion ok");
            lcd.setCursor(0, 1);
            lcd.print("Saldo: $");
            lcd.print(saldo);

        } else {
            
            Serial.println("Saldo insuficiente.");
            Serial.print("Saldo actual: ");
            Serial.println(saldo);

            digitalWrite(LED_ROJO_PIN, HIGH);
            digitalWrite(LED_AZUL_PIN, LOW);

            lcd.clear();
            lcd.setCursor(0, 0);
            lcd.print("Saldo insuficiente");
            lcd.setCursor(0, 1);
            lcd.print("Saldo: $");
            lcd.print(saldo);
        }
    } else {
        
        Serial.println("Tarjeta no autorizada.");
        digitalWrite(LED_ROJO_PIN, HIGH);
        digitalWrite(LED_AZUL_PIN, LOW);

        
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Tarjeta invalida");
    }

    delay(3000);
    digitalWrite(LED_ROJO_PIN, LOW);
    digitalWrite(LED_AZUL_PIN, LOW);

    
    mfrc522.PICC_HaltA();
    mfrc522.PCD_StopCrypto1();
}


bool compareUID(byte *uid, byte *desiredUID, byte uidSize) {
    if (uidSize != 4) { 
        return false;
    }
    for (byte i = 0; i < 4; i++) {
        if (uid[i] != desiredUID[i]) {
            return false;
        }
    }
    return true; 
}
