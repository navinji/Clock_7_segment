import RPi.GPIO as GPIO
import time
import serial
GPIO.setmode(GPIO.BOARD)


def read_card():
    ser = serial.Serial("/dev/ttyUSB0")
    ser.baudrate = 9600
    data = ser.read(5)
    ser.close()
    return data
try:
    while True:
        id = read_card()
        xyz=b'1E005'
        print(xyz)
        print(id)
        if(id==xyz):
            print("Acess granted")
        else:
            print(id)
            print("inside else")
            print("Access Denied")
finally:
    GPIO.cleanup()
                
            
