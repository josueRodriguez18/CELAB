import time
import spidev
import RPi.GPIO as gpio
import wiringpi

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
NUM_ELEMENTS = 1024
out = [None] * NUM_ELEMENTS  #32768 original size (shortened to NUM_ELEMENTS for testing purposes)

spi.writebytes([0xFC]) #sync
time.sleep(1)
spi.writebytes([0x00]) #wakeup

def conversion(value):
	MSB = value[0]
	MidB = value[1]
	LSB = value[2]
	new = (MSB << 16) | (MidB << 8) | (LSB)
	return new

def oneShot():
	wiringpi.piHiPri(3) #program priority higher to reduce overhead
	wiringpi.delayMicroseconds(33) #delay between conversions(30ksps)
	spi.writebytes([0x00]) #WAKEUP command
	while(not gpio.input(drdy) == 0) : #wait until drdy goes low
		pass
	spi.writebytes([0x01]) #READData command
	byteValue = spi.readbytes(3) #read values
	while(not gpio.input(drdy)):
		pass
	spi.writebytes([0xFD]) #put back in standby mode
	return byteValue #return for conversion


def sampler(num):
	spi.writebytes([0xFD]) #begin standby mode (only do once)
	x = 0 #array index
	start = time.clock() #start time for sample
	while x < num: #num samples
		out[x] = conversion(oneShot()) #take sample
		x = x+1 #increment index
	elapsed = time.clock() - start #total elapsed time
	for y in range(0,num):
		print(out[y]) #print out values for testing
	print(elapsed) #print elapsed time (elapsed time/num = deltaX = time between array indeces

