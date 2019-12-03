import math
import pyfftw
from scipy.fftpack import fft
import numpy as np
import spitest
import matplotlib
import matplotlib.pyplot as plt
from spitest import NUM_ELEMENTS
from spitest import out as IN
Fs = 7522

absOut = [None] * NUM_ELEMENTS
def fastFourier():
	input = pyfftw.empty_aligned(NUM_ELEMENTS, dtype ='complex128')
	for i in range(0, NUM_ELEMENTS):
		input[i] = IN[i]
	output = pyfftw.empty_aligned(NUM_ELEMENTS, dtype ='complex128')
	fft_object = pyfftw.FFTW(input, output)
	return output

def max( arr ):
	max = 0
	k = 0
	while k < len(arr):
		if(arr[k] > max):
			max = arr[k]
			pp = k
		k+=1

	return pp
def fourierABS( arr ):
	for x in range(0, NUM_ELEMENTS):
		absOut[x] = math.sqrt(arr[x].real**2 + arr[x].imag**2)
	return absOut



def nFourier():
	x = np.array(IN)
	output = fft(x)
	return output

spitest.main()
outty = nFourier()
absOut = fourierABS(outty)
outty[0] = 0
outty = np.abs(outty)
index = max(outty)
freq = index*Fs/NUM_ELEMENTS
#print(index)
print("Frequency: ")
print(freq)
xaxis = [0]*NUM_ELEMENTS
for i in range (1,NUM_ELEMENTS):
	xaxis[i] = i
plt.plot(xaxis, outty)
plt.show()
