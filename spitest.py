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
<<<<<<< HEAD

out = [None] * 32768  #32768 original size (shortened to 1024 for testing purposes)
=======
NUM_ELEMENTS = 1024
out = [None] * NUM_ELEMENTS  #32768 original size (shortened to NUM_ELEMENTS for testing purposes)
>>>>>>> 2294ddb3d5151edcd57623cb23123a97db69681c

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
	wiringpi.piHiPri(3) #program priority higher to reduce overhead
	wiringpi.delayMicroseconds(33) #delay between conversions(30ksps)
	spi.writebytes([0x00]) #WAKEUP command
	while((gpio.input(drdy)) == 1) : #wait until drdy goes low
		pass
	spi.writebytes([0x01]) #READData command
	byteValue = spi.readbytes(3) #read values
	while((gpio.input(drdy)) == 0):
		pass
	spi.writebytes([0xFD]) #put back in standby mode
	return byteValue #return for conversion


<<<<<<< HEAD
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
=======
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

>>>>>>> 2294ddb3d5151edcd57623cb23123a97db69681c
