#    A Script to control a pwm fan via pigpiod
#
#    Copyright (C) 2024 Julian Stauffer julian.stauffer.js@gmail.com
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#
#install and run "sudo pigpiod" before strting this script
import pigpio #library to use GPIO pins (only one that works with hardware pwm)
import time

pi=pigpio.pi() #initialize the pi
#pi.hardware_PWM(gpio, PWMfreq, PWMduty)
pi.hardware_PWM(12,25000, 450000) #GPIO pin 12, 25khz, 45percent duty
#3percent is the min for be quiet silent wings pro 4
time.sleep(5)
pi.stop()
