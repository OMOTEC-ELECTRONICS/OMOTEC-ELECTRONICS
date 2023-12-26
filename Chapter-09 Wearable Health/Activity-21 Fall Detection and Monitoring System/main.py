from imu import MPU6050
import time
from machine import Pin, I2C

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
imu = MPU6050(i2c)

while True:
    # Following print shows original data get from libary. You can uncomment to see raw data
   # print(imu.accel.xyz,imu.gyro.xyz,imu.temperature,end='\r')
    
    # Following rows round values get for a more pretty print:
    print("Accelarometer value")
    ax=round(imu.accel.x,2)
    ay=round(imu.accel.y,2)
    az=round(imu.accel.z,2)
    print("X",ax,"\t","Y",ay,"\t","z",az)
    print("Gyrometer value")
    gx=round(imu.gyro.x)
    gy=round(imu.gyro.y)
    gz=round(imu.gyro.z)
    print("X",gx,"\t","Y",gy,"\t","z",gz,"\t")
        
    if gx<= 2:
        print ("Fall Detected")
    time.sleep(2) # Following sleep statement makes values enought stable to be seen
