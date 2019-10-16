import time
import spidev
import RPi.GPIO as gpio
import random

spi = spidev.SpiDev()

gpio.setmode(gpio.BOARD)

Gain = 64
Vref = 5.0
bitToVolt = 0

rst = 11
drdy = 13
cs = 15

value = [120, 69, 150]

def read():
	spi.writebytes([0x01])
	value = spi.readbytes(3)
	value = conversion(value)
	return value

def conversion(value):
	MSB = value[0]
	MidB = value[1]
	LSB = value[2]
	new = MSB << 16 | MidB << 8 | LSB
	return new

gpio.setup(rst, gpio.OUT) #RESET
gpio.setup(drdy, gpio.IN) #DRDY
gpio.setup(cs, gpio.OUT) #CS

spi.open(0, 0)

out = [None] * 32768

for i in range(0, 32768):
	if (drdy):
		out[i] = read()
print(value)
value = conversion(value)
print(value)





