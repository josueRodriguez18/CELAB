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

df = 1

spi.open(0, 0)
spi.mode = 1
spi.max_speed_hz = 5000000 #5 MHz

gpio.setwarnings(False)

gpio.setup(rst, gpio.OUT) #RESET
gpio.setup(drdy, gpio.IN) #DRDY
gpio.setup(sync, gpio.OUT) #SYNC

out = [None] * 32768  #32768 original size (shortened to 1024 for testing purposes)

spi.writebytes([0xFC]) #sync
wiringpi.delayMicroseconds(1000000)
spi.writebytes([0x00]) #wakeup

def conversion(value):
	MSB = value[0]
	MidB = value[1]
	LSB = value[2]
	new = (MSB << 16) | (MidB << 8) | (LSB)
	return new

def oneShot():
	#for j in range(0, 46200): #delay between oneShots, not accurate (should be 33 microseconds)
	#	pass #do nothing
	#df = 1 #set data flag to one
	wiringpi.delayMicroseconds(33)
	spi.writebytes([0x00]) #WAKEUP command
	while((gpio.input(drdy)) == 1) : #wait until drdy goes low
		pass
	spi.writebytes([0x01]) #READData command
	byteValue = spi.readbytes(3) #read values
	while((gpio.input(drdy)) == 0):
		pass
	spi.writebytes([0xFD]) #put back in standby mode
	return byteValue #return for conversion


spi.writebytes([0xFD]) #begin standby mode
x = 0 #array index
start = time.clock() #start time for sample
while x < 32768: #1024 samples
	out[x] = conversion(oneShot()) #take sample
	x = x+1 #increment index
elapsed = time.clock() - start #total elapsed time
for y in range(0, 32768):
	print(out[y]) #print out values for testing
print(elapsed) #print elapsed time (elapsed time/1024 = deltaX = time between array indeces
#k = 0
#for y in range(2, 32768): #look for similar values and return the differences between their indexes
#	if out[y] <= out[1] + 5 and out[y] >= out[1] - 5:
#		k = y - 1
#print(k)
xaxis = [0]*32768
for i in range(1,32768):
	xaxis[i] = i
plt.plot(xaxis, out)
plt.show()
