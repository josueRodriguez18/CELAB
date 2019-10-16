import pyfftw
import numpy
import spitest
NUM_ELEMENTS = 32768
Fs = 30000

def fastFourier():
    input = pyfftw.empty_aligned(32768, dtype ='complex128')
    output = pyfftw.empty_aligned(32768, dtype ='complex128')
    fft_object = pyfftw.FFTW(input, output)
    return output

def max( arr ):
    max = 0
    for x in arr:
        if(arr[x] > max):
            max = arr[x]

    return x

def fourierABS( arr ):
    for(x in arr):
        absOut[x] = sqrt(arr[x].real^2 + arr[x].imag^2)
    return absOut