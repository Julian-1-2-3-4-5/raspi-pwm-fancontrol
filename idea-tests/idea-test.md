# Testing Ideas

for my Idea of a python script to turn a Raspberry Pi into a PWM fancontroller to work, i needed a couple parts to work.

1. a way to read the temperature from a sensor
2. a way to control a fan via pwm
3. a way to use a temperature curve

My chosen sensor is a SHT31-D Temperature and Humidity I²C Sensor, but you can probably adapt my scripts to work with any sensor.

To read data from the sensor i first used smbus to communicate directly with the sensor via I²C and then convert the raw output to a human readable temperature and humidity. This script is [tempread_old.py](tempread_old.py)

Then i found out that the easiest solution to use pwm is to use the [pigpiod library](https://abyz.me.uk/rpi/pigpio/), because of the [hardware_PWM](https://abyz.me.uk/rpi/pigpio/python.html#hardware_PWM) function. So i rewrote the tempread-script using pigpiod: This Script is [tempread.py](tempread.py).

The Script to control a pwm fan via pigpiod is pretty straighforward:.[fancontrol.py](fancontrol.py).

To use a temperature curve, i wrote this script .[tempcurve.py](tempcurve.py) which lets one specify points on the curve and then uses linear functions between any two points to find values for points in between them.
