import serial
import time

try:
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
    ser.write(b'\n')
    time.sleep(0.5)
    print(ser.read(1000).decode('utf-8', errors='ignore'))
    ser.close()
except Exception as e:
    print(e)
