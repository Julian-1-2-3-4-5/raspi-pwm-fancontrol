#temp curve points
#temp[x]=Temperature at point; p[x]=PWM-Duty(PWM percent at point)
temp1=25
p1=30000
temp2=35
p2=300000
temp3=45
p3=400000
temp4=50
p4=500000
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
    p=round(p) #p round to be usable for pwm
    return(p)

print(tempcurve(int(input())))