import pyfftw
import numpy
input = pyfftw.empty_aligned(32768, dtype ='complex128')
output = pyfftw.empty_aligned(32768, dtype ='complex128')
fft_object = pyfftw.FFTW(a, b)
