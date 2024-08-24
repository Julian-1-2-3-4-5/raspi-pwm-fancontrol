#    A Script to read Temperature and humidity from an SHT31 sensor via pigpiod
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
#install and run sudo pigpiod before starting this script
import time
import pigpio

pi=pigpio.pi() #initialize the pi

#open i2c connection SHT31 address, 0x44(68)
temp_sensor=pi.i2c_open(1,0x44)

pi.i2c_write_i2c_block_data(temp_sensor,0x2C, [0x06])

time.sleep(0.5)

# SHT31 address, 0x44(68)
# Read data back from 0x00(00), 6 bytes
# Temp MSB, Temp LSB, Temp CRC, Humididty MSB, Humidity LSB, Humidity CRC
data =pi.i2c_read_i2c_block_data(temp_sensor,0x00,6)
data =list(list(data)[1]) #da data eine liste als bytearray der form[anzahl_bytes,bytearray der liste] enthält

# Convert the data

temp = data[0] * 256 + data[1]
Temp = -45 + (175 * temp / 65535.0)
humidity = 100 * (data[3] * 256 + data[4]) / 65535.0

# Output data to screen

print ("Temperature in Celsius is : %.2f C" %Temp)
print ("Relative Humidity is : %.2f %%RH" %humidity)

pi.i2c_close(temp_sensor)
pi.stop()