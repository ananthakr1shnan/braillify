import serial

try:
    ser = serial.Serial("COM7", 9600)
except serial.SerialException as e:
    print("error")
    exit(1)
while True:
    data = ser.readline()
    print(int(data[0])-48)
