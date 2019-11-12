import time
import timeit
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

gpio.setwarnings(False)

gpio.setup(rst, gpio.OUT) #RESET
gpio.setup(drdy, gpio.IN) #DRDY
gpio.setup(sync, gpio.OUT) #SYNC

#value = [120, 69, 150]

out = [None] * 1024  #32768 original size

spi.writebytes([0xFC]) #sync
time.sleep(1)
spi.writebytes([0x00]) #wakeup









def conversion(value):
	MSB = value[0]
	MidB = value[1]
	LSB = value[2]
	new = (MSB << 16) | (MidB << 8) | (LSB)
	return new






def main():
	x = 0 #out index
	t = 1
	drc = 5
	df = 1 #previous data ready state flag
	while(True):
		if (x == 32768): #32768
			for j in range(1, 32768): #32768
				print(out[j])
				print(j)
			break
		if (gpio.input(drdy) == 0 and df == 1): #if data ready just went from high to low
			if(drc == 0):
				spi.writebytes([0x01])
				for y in range(1, 9115): #wait for 6.51 uS = 9115
					pass
				byteValue = spi.readbytes(3)  #take in data
				out[x] = byteValue  #convert
				#print(conversion(byteValue)/(2**24))
				x = x + 1 #increment index
				#print(x)
			df = 0 #update drdy previous state
		if (gpio.input(drdy) == 1 and df == 0):
			drc = drc - 1
			if (drc == 0):
				df = 1
				drc = 5



		#spi.writebytes([0x01]) <-- uncomment this  if you wanna probe the clock output










def tester():
#	testint = 0
#	while(True):
#		spi.writebytes([0x01])
#		start = time.time()
#		for x in range(1, 9115):
#			pass
#
#		#print(elapsed)
#		#counter for delay
#		testint = spi.readbytes(3)
#		print(testint)


	s ='''x = 0
	df = 1 #previous data ready state flag
	while(True):
		if (x == 32768):
			break
		if (gpio.input(drdy) == 0 and df == 1): #if data ready just went from high to low
			spi.writebytes([0x01]) #issue read command
			byteValue = spi.readbytes(3)  #take in data
			out[x] = byteValue  #convert
			x = x + 1 #increment index
			df = 0 #update drdy previous state
		if (gpio.input(drdy) == 1):
			df = 1'''
	print timeit.timeit(stmt = s, number = 100)

#tester()


def oneShot():
	for j in range(0, 46200):
		pass
	df = 1
	spi.writebytes([0x00])
	while(not gpio.input(drdy) == 0) :
		pass
	spi.writebytes([0x01])
	byteValue = spi.readbytes(3)
	return byteValue


spi.writebytes([0xFD])
x = 0
start = time.clock()
while x < 1023:
	out[x] = conversion(oneShot())
	#out[x] = oneShot()
	x = x+1
elapsed = time.clock() - start
for y in range(0,1023):
	print(out[y])
print(elapsed)
k = 0
for y in range(2, 1023):
	if out[y] == out[1]:
		k = y - 1
print(k)
