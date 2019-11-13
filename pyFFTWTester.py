import pyfftw
import numpy
import spitest
import spitest.NUM_ELEMENTS as NUM_ELEMENTS
Fs = 30000

def fastFourier():
    input = pyfftw.empty_aligned(NUM_ELEMENTS, dtype ='complex128')
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
    for x in arr:
        absOut[x] = sqrt(arr[x].real^2 + arr[x].imag^2)
    return absOut

freq = max(fastFourier())*Fs/NUM_ELEMENTS
