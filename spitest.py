import time
import spidev
import RPi.GPIO as gpio
import random

spi = spidev.SpiDev()

gpio.setmode(gpio.BOARD)

rst = 11
drdy = 13
sync = 15

df = 1

spi.open(0, 0)
spi.mode = 1
spi.max_speed_hz = 5000000 #5 MHz

gpio.setup(rst, gpio.OUT) #RESET
gpio.setup(drdy, gpio.IN) #DRDY
gpio.setup(sync, gpio.OUT) #SYNC

#value = [120, 69, 150]

out = [None] * 32768

spi.writebytes([0xFC]) #sync
time.sleep(1)
spi.writebytes([0x00]) #wakeup









def conversion(value):
	MSB = value[0]
	MidB = value[1]
	LSB = value[2]
	new = MSB << 16 | MidB << 8 | LSB
	return new






def main():
	x = 0 #out index
	df = 1 #previous data ready state flag
	while(True):
		if(gpio.input(drdy) == 0 and df == 1): #if data ready just went from high to low
			df = 0 #update drdy previous state
			spi.writebytes([0x01]) #issue read command
#			time.sleep(.00000651) #amount of time for 50 clock pulse delay (Rclk/Sclk x 50)
			byteValue = spi.readbytes(3)  #take in data
			out[x] = conversion(byteValue) #convert
			print(byteValue)
			x = x + 1 #increment index
		if (gpio.input(drdy) == 1):
			df = 1


		#spi.writebytes([0x01]) <-- uncomment this  if you wanna probe the clock output

#main()

testint = 0

while(True):
	spi.writebytes([0x01])
	time.sleep(.000002)
	testint = spi.readbytes(3)
	#print(testint)
df = 1
#while(True):
#	if(gpio.input(drdy) == 0 and df == 1): #if data ready just went from high to low
#	if(gpio.input(drdy) == 0): #non df based if statement
#		df = 0 #update drdy previous state
#		spi.writebytes([0x01]) #issue read command
		#time.sleep(.0001) #amount of time for 50 clock pulse delay (Rclk/Sclk x 50)
	#	byteValue = spi.readbytes(3)  #take in data
#	if (gpio.input(drdy) == 1):
#		df = 1




