import time
import platform

# Simulación de pines GPIO si no estamos en una Raspberry Pi
class MockGPIO:
    OUT = 0
    HIGH = 1
    LOW = 0

    @staticmethod
    def setwarnings(flag):
        pass

    @staticmethod
    def setmode(mode):
        pass

    @staticmethod
    def setup(pin, mode):
        pass

    @staticmethod
    def output(pin, state):
        print(f"Simulando cambio de pin {pin} a {'HIGH' if state == MockGPIO.HIGH else 'LOW'}")

    @staticmethod
    def cleanup():
        print("Limpiando configuración de pines.")

# Simulación de un lector RFID
class MockMFRC522:
    def read(self):
        # Simula un UID de una tarjeta RFID
        return 0x436F2716, "Simulando tarjeta"  # Simula un UID específico

# Simulación de LCD si no estamos en Raspberry Pi
class MockLCD:
    def __init__(self):
        pass

    def init(self):
        print("Simulando inicialización del LCD.")

    def clear(self):
        print("Simulando limpieza del LCD.")

    def write(self, message, line):
        print(f"Simulando escritura en el LCD: {message} en la línea {line}")

# Usar la simulación de GPIO, MFRC522 y LCD si no estamos en una Raspberry Pi
if platform.system() == 'Linux' and 'raspberrypi' in platform.node():
    from RPi import GPIO
    from mfrc522 import SimpleMFRC522
    from smbus2 import SMBus
    reader = SimpleMFRC522()
    lcd = SMBus(1)
else:
    GPIO = MockGPIO  # Usamos la simulación de GPIO
    reader = MockMFRC522()  # Usamos la simulación de RFID
    lcd = MockLCD()  # Usamos la simulación de LCD

# Configuración de pines GPIO para LEDs
LED_ROJO_PIN = 7
LED_AZUL_PIN = 6

# Configuración de saldo y UID esperado
desired_uid = [0x43, 0x6F, 0x27, 0x16]
saldo = 5.0
COSTO = 10.0

# Inicializar LCD
lcd.init()

def lcd_clear():
    lcd.clear()

def lcd_write(message, line):
    lcd.write(message, line)

# Configurar pines GPIO para los LEDs
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_ROJO_PIN, GPIO.OUT)
GPIO.setup(LED_AZUL_PIN, GPIO.OUT)

try:
    while True:
        lcd_write("Pase tarjeta", 1)
        print("Aproxime la tarjeta...")

        # Simulación de lectura de tarjeta RFID (sin hardware real)
        uid, text = reader.read()  # Lee el UID de la tarjeta (simulado)
        uid_bytes = [int(byte) for byte in hex(uid)[2:].zfill(8)]

        print(f"UID leído: {uid_bytes}")
        lcd_clear()

        if uid_bytes == desired_uid:
            if saldo >= COSTO:
                saldo -= COSTO
                GPIO.output(LED_AZUL_PIN, GPIO.HIGH)
                GPIO.output(LED_ROJO_PIN, GPIO.LOW)

                lcd_write("Transaccion ok", 1)
                lcd_write(f"Saldo: ${saldo:.2f}", 2)
                print("Transacción exitosa. Nuevo saldo:", saldo)
            else:
                GPIO.output(LED_ROJO_PIN, GPIO.HIGH)
                GPIO.output(LED_AZUL_PIN, GPIO.LOW)

                lcd_write("Saldo insuficiente", 1)
                lcd_write(f"Saldo: ${saldo:.2f}", 2)
                print("Saldo insuficiente. Saldo actual:", saldo)
        else:
            GPIO.output(LED_ROJO_PIN, GPIO.HIGH)
            GPIO.output(LED_AZUL_PIN, GPIO.LOW)

            lcd_write("Tarjeta invalida", 1)
            print("Tarjeta no autorizada.")

        time.sleep(3)
        GPIO.output(LED_ROJO_PIN, GPIO.LOW)
        GPIO.output(LED_AZUL_PIN, GPIO.LOW)
        lcd_clear()

except KeyboardInterrupt:
    print("Programa detenido.")
    lcd_clear()
    lcd_write("Apagando...", 1)
    GPIO.cleanup()
