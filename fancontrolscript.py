#install and run sudo pigpiod before starting this script
import pigpio #library to use GPIO pins (only one that works with hardware pwm)
import time

pi=pigpio.pi() #initialize the pi 

#variables-----------------------------
#temp curve points
#temp[x]=Temperatur des Punktes; p[x]=PWM-Duty(Percent des Punktes)
temp1=20
p1=30000
temp2=35
p2=300000
temp3=45
p3=400000
temp4=60
p4=800000
temp5=70
p5=1000000

#interpolate linear function (like a tempcurve)
def tempcurve(given_temp):
    #import variables into local namespace
    global temp1 
    global p1
    global temp2
    global p2
    global temp3
    global p3
    global temp4
    global p4
    global temp5
    global p5
    if given_temp <= temp1: #below the first point the fan's not spinning
        p=0
    elif given_temp<=temp2: # between point 1 and 2
        p=p1+((p2-p1)/(temp2-temp1))*(given_temp-temp1) #interpolate linear function between 1 and 2
    elif given_temp<=temp3:
        p=p2+((p3-p2)/(temp3-temp2))*(given_temp-temp2) #interpolate linear function between 2 and 3
    elif given_temp<=temp4:
        p=p3+((p4-p3)/(temp4-temp3))*(given_temp-temp3) #interpolate linear function between 3 and 4
    elif given_temp<=temp5:
        p=p4+((p5-p4)/(temp5-temp4))*(given_temp-temp4) #interpolate linear function between 4 and 5
    elif given_temp>=temp5: #above the last point, the fan's spinnijng at max speed
        p=1000000
    else:
        print("temp not readeable")
    p=round(p) # round p to be able to use it as a PWM Value
    return(p)


#set pwm speed
#pi.hardware_PWM(gpio, PWMfreq, PWMduty)
def set_speed(p):
    pi.hardware_PWM(12,25000, p) #GPIO pin 12, 25khz, p duty
    return()

#get temperature from sensor
def get_temp():
    
    #open i2c connection SHT31 address, 0x44(68)
    temp_sensor=pi.i2c_open(1,0x44)

    pi.i2c_write_i2c_block_data(temp_sensor,0x2C, [0x06])

    time.sleep(0.5)

    # SHT31 address, 0x44(68)
    # Read data back from 0x00(00), 6 bytes
    # Temp MSB, Temp LSB, Temp CRC, Humididty MSB, Humidity LSB, Humidity CRC
    data =pi.i2c_read_i2c_block_data(temp_sensor,0x00,6)
    data =list(list(data)[1]) #da data eine liste als bytearray der form[anzahl_bytes,bytearray der liste] enthält
    pi.i2c_close(temp_sensor)#close the i2c connection
    
    #convert data
    temp = data[0] * 256 + data[1]
    Temp = -45 + (175 * temp / 65535.0)
    
    return(Temp)

while True:
    Temp1=get_temp() #get temperature from sensor
    time.sleep(0.2)
    Temp2=get_temp() #get temperature from sensor
    Temp=(Temp1+Temp2)/2 #calculate mean temperature (to prefent fan speeds changing rapidly)
    
    speed=tempcurve(Temp) #calculate speed from temperature
    set_speed(speed) #set pwm speed of fans
    #print(str(Temp1) +","+ str(Temp2) +";"+ str(Temp) +":"+ str(speed))
pi.stop()