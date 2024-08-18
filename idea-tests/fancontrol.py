#install and run "sudo pigpiod" before strting this script
import pigpio #library to use GPIO pins (only one that works with hardware pwm)
import time

pi=pigpio.pi() #initialize the pi
#pi.hardware_PWM(gpio, PWMfreq, PWMduty)
pi.hardware_PWM(12,25000, 450000) #GPIO pin 12, 25khz, 45percent duty
#3percent is the min for be quiet silent wings pro 4
time.sleep(5)
pi.stop()
