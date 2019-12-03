import time
import spidev
import RPi.GPIO as gpio
import wiringpi
import matplotlib
import matplotlib.pyplot as plt

spi = spidev.SpiDev()

gpio.setmode(gpio.BOARD)

rst = 11
drdy = 13
sync = 15
timer = 16

NUM_ELEMENTS = 4096+4096

spi.open(0, 0)
spi.mode = 1
spi.max_speed_hz = 5000000 #5 MHz

gpio.setwarnings(False)

gpio.setup(rst, gpio.OUT) #RESET
gpio.setup(drdy, gpio.IN) #DRDY
gpio.setup(sync, gpio.OUT) #SYNC
gpio.setup(timer, gpio.IN) #555 Timer

out = [None] * NUM_ELEMENTS  #32768 original size (shortened to 1024 for testing purposes)

spi.writebytes([0xFC]) #sync
spi.writebytes([0x00]) #wakeup

def conversion(value):
	#this number is in 2's comp format
	MSB = value[0]
	MidB = value[1]
	LSB = value[2]
	new = (MSB << 16) | (MidB << 8) | (LSB)
	sign = MSB & 0b10000000 #check sign bit to see if complement is necessary
	sign = sign >> 7
	if sign: #2's comp
		new = ~new
		new = new + 0b1
	return new

def oneShot():
	count(7) #count x 33 us periods
	spi.writebytes([0x00]) #WAKEUP command
	while((gpio.input(drdy)) == 1) : #wait until drdy goes low
		pass
	spi.writebytes([0x01]) #READData command
	byteValue = spi.readbytes(3) #read values
	while((gpio.input(drdy)) == 0):
		pass
	spi.writebytes([0xFD]) #put back in standby mode
	return byteValue #return for conversion

def count(y):
	df = 0 #data flag to count rises
	x = 0
	while(x < y): # num*3 equals 33 us periods
		if(gpio.input(timer) == 1 and df == 0): #rise
			x = x + 1 #increment counter
			df = 1 #reset df
		if (gpio.input(timer) == 0 and df == 1): #fall
			df = 0 #reset df

def main():
	spi.writebytes([0xFD]) #begin standby mode
	x = 0 #array index
	#start = time.clock() #start time for sample
	while x < NUM_ELEMENTS: #1024 samples
		out[x] = conversion(oneShot()) #take sample
		x = x+1 #increment index
	#elapsed = time.clock() - start #total elapsed time
	#avgel = elapsed/NUM_ELEMENTS
	#for y in range(0, NUM_ELEMENTS):
	#	print(out[y]) #print out values for testing
	#print(elapsed) #print elapsed time (elapsed time/1024 = deltaX = time between array indeces
	#print(avgel)
	#xaxis = [0]*NUM_ELEMENTS
	#for i in range(1,NUM_ELEMENTS):
	#	xaxis[i] = i
	#plt.plot(xaxis, out)
	#plt.show()
	#arayout = matplotlib.pyplot.specgram(out, 1024, 30000, 0)
	#plt.plot()
main()
