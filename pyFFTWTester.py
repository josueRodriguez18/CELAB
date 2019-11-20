import math
import pyfftw
import numpy
import spitest
from spitest import NUM_ELEMENTS
from spitest import out as IN
Fs = 30000

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
		k+=1
	return k

def fourierABS( arr ):
	for x in range(0, NUM_ELEMENTS):
		absOut[x] = math.sqrt(arr[x].real**2 + arr[x].imag**2)
	return absOut

freq = max(fastFourier())*Fs/NUM_ELEMENTS
spitest.main()
print(max(fourierABS(fastFourier())))
