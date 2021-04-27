import serial
import time


port="/dev/tty.HC-06-DevB"

bluetooth=serial.Serial(port, 9600)
print("conectado")
bluetooth.flushInput()

for i in range(10):
    input_data = bluetooth.readline()
    print(input_data)

bluetooth.close()
