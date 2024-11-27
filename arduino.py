import serial
import time

def conexion_arduino():
    arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)  # Cambia COM3 por tu puerto
    time.sleep(2)  # Espera 2 segundos para que Arduino se estabilice
    return arduino